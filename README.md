whoapi-python
=============

This library interacts with the [WhoAPI](http://www.whoapi.com) service. It allows you to use the REST API in a pythonic way to query the WhoAPI service.


Installation
------------

Download the latest source here:  [tar.gz](https://github.com/danielwren/whoapi-python/tarball/master) 
or checkout the code, then `cd` into the resulting directory and run `python setup.py install`.

Usage
-----

Instantiate a Demo WhoAPI object:   `WhoAPI('demokey')`

Instantiate a WhoAPI object:        `WhoAPI('my_api_key')`

Perform a basic query:              `query('domain.tld', 'api_function')`


Quick Start
-----------

WhoAPI Key can be found at [Account Details](http://whoapi.com/myaccount.html)

```
from whoapi import WhoAPI
import pprint

# Instantiate object, providing your API key
whoapi = WhoAPI('demokey')

print "\n----- Whois -----\n"
# Arguments:  domain, function
pprint.pprint(whoapi.query('whoapi.com', 'whois'))

print "\n----- Is Domain Available? -----\n"
print whoapi.isDomainAvailable('whoapi.com')
```

See test queries in /examples/test.py.

Note
----
- As of 02/17/2014, WhoAPI does not currently support look-up for the new gTLDs.
- A complete list of functions is available at:  https://whoapi.com/api-functions.html
- 'demokey' can only be used for domain 'whoapi.com'

