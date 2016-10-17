################
Instance methods
################
* Authorization
* Current User
* Users
* Photos
* Categories
* Collections
* Stats

Authorization
=============
TODO


Current User
============
TODO


Users
=====
**users.get(username, w, h)**
    Retrieve public details on a given user.
    Supplying the optional *w* or *h* parameters will result in the custom photo URL being added to the profile_image object.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    w           number    optional
    h           number    optional
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get(username='salvoventura')

----

**users.get_portfolio(username)**
    Retrieve a single user's portfolio link.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_portfolio(username='salvoventura')
        portfolio_url = json_body.get('url')

----


Photos
======



Categories
==========



Collections
===========



Stats
=====
