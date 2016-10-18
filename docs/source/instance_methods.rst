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
        json_body = pu.users.get(username='<username>')

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
        json_body = pu.users.get_portfolio(username='<username>')
        portfolio_url = json_body.get('url')

----

**users.get_following(username)**
    API location of users this user is following.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_following(username='<username>')

----

**users.get_followers(username)**
    API location of this user's followers.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_followers(username='<username>')

----

**users.get_photos(username, page, per_page, order_by)**
    Get a list of photos uploaded by a user.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    username    string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    order_by    string    optional (default: latest)    latest, oldest, popular
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=1, per_page=5, order_by='popular')

----

**users.get_likes(username, page, per_page, order_by)**
    Get a list of photos liked by a user.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    username    string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    order_by    string    optional (default: latest)    latest, oldest, popular
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=1, per_page=5, order_by='popular')

----

**users.get_collections(username, page, per_page)**
    Get a list of collections created by the user.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    username    string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_collections(username='<username>', page=1, per_page=2)

----

Photos
======



Categories
==========



Collections
===========



Stats
=====
