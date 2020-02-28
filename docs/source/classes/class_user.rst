###############
API: Class User
###############
This class is used to interact with the ``Unsplash`` ``/users/:username`` REST API.

The constructor is invoked through the main ``PyUnsplash`` class as ``PyUnsplash.user(username, w, h)``

======================
Methods and properties
======================
Methods and properties exposed by the ``User`` class.

**User.refresh()**
------------------
    Reload the full object from its REST API URI. Required if there has been an update
    to the object, or if you need to retrieve the full object starting from a simplified
    content copy coming from a list.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    None
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        this_user.refresh()

--------

**User.id**
-----------
    Unique identifier for this user resource.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **string**  unique resource identifier
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.id

--------

**User.links**
--------------
    Dictionary of the ``links`` section in the resource body.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **dict**    links section from the resource body
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.links

--------

**User.link_html**
------------------
    Link to the html representation of the resource.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ==============================================
    **string**  url to the html representation of the resource
    ==========  ==============================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.link_html

--------

**User.link_portfolio**
-----------------------
    Link to the user specified portfolio page.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **string**  url to the user portfolio
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.link_portfolio

--------

**User.link_followers**
-----------------------
    API location of this user's followers.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ================================================
    **string**  url to the API location of this user's followers
    ==========  ================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.link_followers

--------

**User.link_following**
-----------------------
    API location of users this user is following.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================================
    **string**  url to the API location of users this user is following
    ==========  =======================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.link_following

--------

**User.link_photos**
--------------------
    API location of this user's photos.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =============================================
    **string**  url to the API location of this user's photos
    ==========  =============================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        print this_user.link_photos

--------

**User.photos(page, per_page, order_by)**
-----------------------------------------
    Allows easy access to each photo from this user.
    Returns ``Photos`` collection object from this user's ``link_photos`` url.

    **Parameters**

    ============  ======  ==========================  ====================================
    Argument      Type    Optional/Required           Notes
    ============  ======  ==========================  ====================================
    **page**      number  optional (default: 1)       Page number to retrieve.
    **per_page**  number  optional (default: 10)      Number of items per page (max: 30)
    **order_by**  string  optional (default: latest)  latest, oldest, popular
    ============  ======  ==========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``Photos``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        photos = this_user.photos(per_page=5)
        for photo in photos.entries:
            print photo.id, photo.link_download

--------

**User.followers()**
--------------------
    Allows easy access to each user that is a follower of this user.
    Returns ``Users`` collection object from this user's ``link_followers`` url.

    **Parameters**

    ============  ======  ==========================  ====================================
    Argument      Type    Optional/Required           Notes
    ============  ======  ==========================  ====================================
    N/A
    ============  ======  ==========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``Users``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        followers = this_user.followers()
        for user in followers.entries:
            print user.id, user.body.get('first_name'), user.body.get('last_name')

--------

**User.following()**
--------------------
    Allows easy access to each user that is followed by this user.
    Returns ``Users`` collection object from this user's ``link_following`` url.

    **Parameters**

    ============  ======  ==========================  ====================================
    Argument      Type    Optional/Required           Notes
    ============  ======  ==========================  ====================================
    N/A
    ============  ======  ==========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``Users``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        following = this_user.following()
        for user in following.entries:
            print user.id, user.body.get('first_name'), user.body.get('last_name')

--------

**User.likes(page, per_page, order_by)**
----------------------------------------
    Allows easy access to each photo liked by this user.
    Returns ``Photos`` collection object.

    **Parameters**

    ============  ======  ==========================  ====================================
    Argument      Type    Optional/Required           Notes
    ============  ======  ==========================  ====================================
    **page**      number  optional (default: 1)       Page number to retrieve.
    **per_page**  number  optional (default: 10)      Number of items per page (max: 30)
    **order_by**  string  optional (default: latest)  latest, oldest, popular
    ============  ======  ==========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``Photos``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        photos = this_user.likes(per_page=5)
        for photo in photos.entries:
            print photo.id, photo.link_download

--------

**User.collections(page, per_page, order_by)**
----------------------------------------------
    Allow easy access to the collections created by this user.
    Returns ``Collections`` object.

    **Parameters**

    ============  ======  ==========================  ====================================
    Argument      Type    Optional/Required           Notes
    ============  ======  ==========================  ====================================
    **page**      number  optional (default: 1)       Page number to retrieve.
    **per_page**  number  optional (default: 10)      Number of items per page (max: 30)
    ============  ======  ==========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``Collections``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        collections = this_user.collections(page=1, per_page=5)
        for collection in collections.entries:
            print collection.id, collection.title


--------

**User.statistics(resolution, quantity)**
----------------------------------------------
    Retrieve the consolidated number of downloads, views and likes of this user's photos,
    as well as the historical breakdown and average of these stats in a specific timeframe (default is 30 days).

    Returns ``UserStatistics`` object.

    **Parameters**

    ==============  ======  ============================  ====================================
    Argument        Type    Optional/Required             Notes
    ==============  ======  ============================  ====================================
    **resolution**  number  optional (default: ``days``)  The frequency of the stats.
    **quantity**    number  optional (default: 30)        The amount of for each stat.
    ==============  ======  ============================  ====================================

    **NOTE** Currently, the only resolution param supported is ``days`` and the quantity param
    can be any number between 1 and 30.

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``UserStatistics``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        user_statistics = this_user.statistics()

--------

**User.body**
--------------
    This is the full object returned by the API in JSON format.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ============================================
    **string**  User object returned by API, in JSON format
    ==========  ============================================
