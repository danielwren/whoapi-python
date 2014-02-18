from whoapi import WhoAPI
import pprint

def main():
    
    #demokey only works for domain whoapi.com
    whoapi = WhoAPI('whoapi.com')
    
    print "\n----- Is Domain Available -----\n"
    print whoapi.isDomainAvailable('whoapi.com')
    
    print "\n----- Whois -----\n"
    pprint.pprint(whoapi.query('whoapi.com', 'whois'))
    
    print "\n----- Ranks -----\n"
    pprint.pprint(whoapi.query('whoapi.com', 'ranks'))


if __name__ == '__main__':
    main()