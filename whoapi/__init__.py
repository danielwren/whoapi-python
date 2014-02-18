
import os, logging, re, json, requests
from whoapi import exceptions, constants

class WhoAPI(object):
    
    OPTIONAL_PARAMS = ['rr', 'ip', 'port', 'fullurl']

    def __init__(self, apiKey='demokey'):
        self._apiKey = apiKey

    def query(self, *args, **kwargs):
        
        requestParams = self.getRequestParams(*args, **kwargs)
        request = requests.get(
            constants.WHOAPI_BASE_URL, 
            params=requestParams)

        logging.debug("[WhoAPI.query] Request URL : %s" % request.url)
        logging.debug("[WhoAPI.query] Response Status Code : %s" % request.status_code)
        logging.debug("[WhoAPI.query] Response Content : %s" % request.content)

        content = json.loads(request.content)

        try:
            statusCode = content['status']

            if str(statusCode) not in ( '0' ):
                raise exceptions.ResponseError(content['status_desc'], error_code=statusCode)

        except (KeyError, AttributeError) as e:
            if len(content) < 3: # Because status is not returned with every so we gotta count in case there are more than 2 items in object
                    raise Exception("WhoAPI is probably down or under some heavy bug. Please contact WhoAPI support.")
                    
        return content
        

    def getRequestParams(self, *args, **kwargs):
        requestParams = {}
        
        # Required - Implicit arguments
        if(self.validate('apikey', self._apiKey)):
            requestParams['apikey'] = self._apiKey
        
        # Required - Domain argument
        if(self.validate('domain', args[0])):
            requestParams['domain'] = args[0]
        
        # Required - Request argument            
        if(self.validate('r', args[1])):
            requestParams['r'] = args[1]
            
        # Optional - Dictionary arguments
        for key, value in kwargs.iteritems():
            if(key in WhoAPI.OPTIONAL_PARAMS):
                if(value is not None):
                    if(self.validate(key, value)):
                        requestParams[key] = value
                        
        return requestParams

    
    ### Convenience ###    
        
    def isDomainAvailable(self, domain):
        available = None
        content = self.query(domain, 'taken')
        
        if(content['taken'] == '0'): 
            available = True
        else: 
            available = False
        
        return available
        
        
    
    ### Validation ###
    
    def validate(self, param, value):

        if(param == 'apikey'):
            isApiKeyValid = self._isValidApiKey(value)
            logging.debug("[WhoAPI.validate] Is API key valid? (%s)" % isApiKeyValid)
            if not isApiKeyValid:
                raise exceptions.KeyError('In order to query against WhoAPI you will need to provide valid WhoAPI key.')
            else:
                return True

        elif(param == 'domain'):
            isDomainValid = self._isValidDomain(value)
            logging.debug("[WhoAPI.validate] Is domain valid? (%s)" % isDomainValid)
            if not isDomainValid:
                raise exceptions.DomainError('In order to query against WhoAPI you will need to provide valid domain.')
            else:
                return True
                
        elif(param == 'r'):
            isRequestValid = self._isValidRequest(value)
            logging.debug('[WhoAPI.validate] Is request type valid? (%s)' % isRequestValid)
            if not isRequestValid:
                raise exceptions.RequestTypeError('Invalid request type provided')
            else:
                return True
                
        elif(param == 'rr'):
            # TODO - Add validation checks
            return True
            
        elif(param == 'ip'):
            # TODO - Add validation checks
            return True
            
        elif(param == 'port'):
            # TODO - Add validation checks
            return True
            
        elif(param == 'fullurl'):
            # TODO - Add validation checks
            return True
            
        else:
            # TODO - Raise error
            pass

    def _isValidApiKey(self, apikey):
        if len(apikey) < 32 and apikey != 'demokey':
            return False
        else:
            return True        


    def _isValidDomain(self, domain):

        logging.debug("[WhoAPI.is_valid_domain] Looking if %s is valid or not ..." % domain)
        
        # TODO - This regex will need to be updated to handle the new gTLDs
        # Note - As of 02/17/2014, WhoAPI does not currently support he new gTLDs and support states that it is not a priority for support to be added for them
        domain_regex = re.compile(r'^(?=.{4,255}$)([a-zA-Z0-9][a-zA-Z0-9-]{,61}[a-zA-Z0-9]\.)+[a-zA-Z0-9]{2,5}$')
        match = re.match(domain_regex, domain)
        if match: return True
        return False
        

    def _isValidRequest(self, request_type):
        logging.debug("[WhoAPI.is_valid_request] Looking if %s is valid request or not ..." % request_type)
        return request_type in constants.WHOAPI_REQUEST_TYPES
