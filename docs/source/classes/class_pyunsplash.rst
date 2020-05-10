#####################
API: Class PyUnsplash
#####################
This is the main class used to interact with the ``Unsplash`` REST API.

=======================
**PyUnsplash(api_key)**
=======================
    Create an instance of class ``PyUnsplash``.
    The ``api_key`` parameter is required.
    API keys can be obtained from `Unsplash Developers <https://unsplash.com/developers>`_.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    **api_key**   string  required                  Your application ID
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``PyUnsplash``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

---------


======================
Methods and properties
======================
Methods and properties exposed by the ``PyUnsplash`` class.

**PyUnsplash.user(username, w, h)**
-----------------------------------
    To interact with the ``user`` API, create an instance of class ``User``.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    **username**  string  required                  The user's username.
    **w**         number  optional                  Profile image width in pixels.
    **h**         number  optional                  Profile image height in pixels.
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **Object**  Instance of class ``User``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)

--------

**PyUnsplash.collections(type_, page, per_page)**
-------------------------------------------------
    To interact with the ``collections`` API, create an instance of class ``Collections``.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **type_**     string  optional (default: generic)  ``generic``, ``featured`` (``curated`` has been deprecated)
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 10)       Number of items per page (max: 30)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Collections``, ``CuratedCollections``, or
                ``FeaturedCollections`` depending on the value of ``type``

                **NOTE** ``curated`` endpoint has been deprecated by Unsplash
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        # retrieve a page from the featured collections, with a maximum
        # of 5 collections per-page
        collections_page = pu.collections(type_='featured', per_page=5)

--------

**PyUnsplash.photos(type_, page, per_page, order_by)**
------------------------------------------------------
    To interact with the ``photos`` API, create an instance of class ``Photos``.

    **NOTE** ``curated`` endpoint has been deprecated by Unsplash

*Generic Photos*
^^^^^^^^^^^^^^^^

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **type_**     string  optional (default: generic)  ``generic``
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 10)       Number of items per page (max: 30)
    **order_by**  string  optional (default: latest)   ``latest``, ``oldest``, ``popular``
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Photos`` depending on the value of ``type``

                **NOTE** ``curated`` endpoint has been deprecated by Unsplash
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        # retrieve a page from the generic photos, with a maximum
        # of 15 photos per-page
        collections_page = pu.photos(type_='generic', per_page=15)


*Random Photos*
^^^^^^^^^^^^^^^^

    **Parameters**

    ===============  ======  ===========================  ====================================
    Argument         Type    Optional/Required            Notes
    ===============  ======  ===========================  ====================================
    **type_**        string  required                     ``random``
    **collections**  string  optional                     Public collection ID(s) to filter selection
                                                          If multiple, comma-separated
    **featured**     bool    optional                     Limit selection to featured photos
                                                          Completely remove if you don't want featured
                                                          Setting to False doesn't work
    **username**     string  optional                     Limit selection to a single user
    **query**        string  optional                     Limit selection to photos matching a search term
    **orientation**  string  optional                     ``landscape``, ``portrait``, ``squarish``
    **count**        number  required                     Number of items per page (max: 30)
    ===============  ======  ===========================  ====================================

    **Note** You can't use the ``collections`` and ``query`` parameters in the same call


    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``RandomPhotos``
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        # retrieve 4 random photos, which are featured, and tagged as "dog"
        collections_page = pu.photos(type_='random', count=4, featured=True, query="dog")
        for photo in photos.entries:
            print(photo.id, photo.link_download)

--------

*Single Photo*
^^^^^^^^^^^^^^^^

    **Parameters**

    ===============  ======  ===========================  ====================================
    Argument         Type    Optional/Required            Notes
    ===============  ======  ===========================  ====================================
    **type_**        string  required                     ``single``
    **photo_id**     string  required                     ID of the photo you want to load
    ===============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``SinglePhoto``
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        # retrieve specific photo by its ID, and print the attribution
        photo = py_un.photos(type_="single", photo_id='l0_kVknpO2g')
        print(photo.entries.get_attribution(format='txt'))
        print(photo.entries.get_attribution(format='html'))


--------

**PyUnsplash.search(type_, type, page, per_page, query)**
---------------------------------------------------------
    To interact with the ``search`` API, create an instance of class ``Search``.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **type_**     string  required                     ``photos``, ``collections``, ``users``
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 10)       Number of items per page (max: 30)
    **query**     string  optional                     Search terms
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Search``
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        #
        #
        search = pu.search(type_='photos', query='red,car')
        for entry in search.entries:
            print entry.link_html

--------

**PyUnsplash.stats()**
----------------------
    To interact with the ``stats`` API, create an instance of class ``Stats``.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    N/A
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Stats``
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        stats = pu.stats()
        print stats.total   # this is json


