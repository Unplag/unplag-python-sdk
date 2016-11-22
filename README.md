UNPLAG Python Library
===================

This library eases the use of the Unplag REST API from Python and it has been used in production for years.

As this is an open-source project that is community maintained, do not be surprised if some bugs or features are not implemented quickly enough.

Quickstart
----------

Feeling impatient? I like your style.


        from unplag import Unplag

        un = Unplag('api_key', 'api_secret')

        un.file.upload('~/Downloads/original.pdf')
        
        un.file.get(4354)
        
        un.check.create(93345)
        
        un.check.get(93345)