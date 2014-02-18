whoapi-python
=============

This library interacts with the [WhoAPI](http://www.whoapi.com) service. It allows you to use the REST API in a pythonic way to query the WhoAPI service.


Installation
------------

Download the latest source from https://github.com/0x19/whoapi-python/tarball/master or checkout the code, 
then `cd` into the resulting directory and run `python setup.py install`.

Usage
-----

Instantiate a Demo WhoAPI object:   `WhoAPI('demokey')`
Instantiate a WhoAPI object:        `WhoAPI('my_api_key')`
Perform a basic query:              `query('domain.tld', 'api_function')`


Quick Start
-----------

WhoAPI Key can be found at [Account Details](http://whoapi.com/myaccount.html)

``
from whoapi import WhoAPI
import pprint

whoapi = WhoAPI('whoapi.com')

print "\n----- Whois -----\n"
pprint.pprint(whoapi.query('whoapi.com', 'whois'))

print "\n----- Is Domain Available? -----\n"
print whoapi.isDomainAvailable('whoapi.com')
``

See test queries in /examples/test.py.

Note
----
As of 02/17/2014, WhoAPI does not currently support look-up for the new gTLDs and adding the functionality is not a prioritized feature.


