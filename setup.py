from setuptools import setup, find_packages

from whoapi     import constants

def main():
    setup(
        name                = 'whoapi',
        version             = constants.WHOAPI_PACKAGE_VERSION,
        
        orig_author         = 'Nevio Vesic',
        orig_author_email   = 'me@neviovesic.com',
        orig_download_url   = 'https://github.com/0x19/whoapi-python/tarball/master',
        
        author              = 'Daniel Wren',
        author_email        = 'daniel@danielwren.com',
        license             = 'MIT',
        description         = "A python helper for whoapi service.",
        long_description    = 'WhoAPI is service for mass requests of domain information like domain registration availability, structured whois data in XML and JSON, etc.',
        url                 = "http://www.whoapi.com/",
        download_url        = ''
        packages            = find_packages(),
        install_requires    = ['requests'],
        classifiers         = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],        
    )


if __name__ == '__main__':
    main()