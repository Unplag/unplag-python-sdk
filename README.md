UNPLAG Python Library
===================

[![Build Status](https://api.travis-ci.org/Unplag/unplag-python-sdk.svg?branch=master)](https://travis-ci.org/Unplag/unplag-python-sdk)

[![Coverage Status](https://coveralls.io/repos/github/Unplag/unplag-python-sdk/badge.svg)](https://coveralls.io/github/Unplag/unplag-python-sdk)

[![PyPI version](https://badge.fury.io/py/unplag.svg)](https://badge.fury.io/py/unplag)

This library eases the use of the Unplag REST API from Python and it has been used in production for years.

As this is an open-source project that is community maintained, do not be surprised if some bugs or features are not implemented quickly enough.

Quickstart
----------

Installation

    sudo pip install unplag

Feeling impatient? I like your style.

    from unplag import Unplag

    un = Unplag('api_key', 'api_secret')    # Creating connection

    upload = un.file.upload('~/Downloads/original.pdf')     # Upload file from path
    
    check = un.check.create_sync(upload_resp.response['file']['id'])    # Start check using upload id 


Short syntax
------------

    from unplag import Unplag

    un = Unplag('api_key', 'api_secret')
    
    un.check.create_sync(un.file.upload('~/Downloads/original.pdf').response['file']['id']).response
