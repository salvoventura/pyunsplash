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
    **api_key**   string  required
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

**PyUnsplash.collections(type, page, per_page)**
------------------------------------------------
    To interact with the ``collections`` API, create an instance of class ``Collections``.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **type**      string  optional (default: generic)  generic, curated, featured
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 10)       Number of items per page (max: 30)
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Collections``, ``CuratedCollections``, or
                ``FeaturedCollections`` depending on the value of ``type``
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        # retrieve a page from the featured collections, with a maximum
        # of 5 collections per-page
        collections_page = pu.collections(type='featured', per_page=5)

--------

**PyUnsplash.photos(type, page, per_page, order_by)**
-----------------------------------------------------
    To interact with the ``photos`` API, create an instance of class ``Photos``.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **type**      string  optional (default: generic)  generic, curated, random
    **page**      number  optional (default: 1)        Page number to retrieve.
    **per_page**  number  optional (default: 10)       Number of items per page (max: 30)
    **order_by**  string  optional (default: latest)   latest, oldest, popular
    ============  ======  ===========================  ====================================

    **Returns**

    ==========  ========================================================================
    **Object**  Instance of class ``Photos``, ``CuratedPhotos``, or ``RandomPhotos``
                depending on the value of ``type``
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')

        # retrieve a page from the curated photos, with a maximum
        # of 15 photos per-page
        collections_page = pu.photos(type='curated', per_page=15)

--------

**PyUnsplash.search(type, type, page, per_page, query)**
--------------------------------------------------------
    To interact with the ``search`` API, create an instance of class ``Search``.

    **Parameters**

    ============  ======  ===========================  ====================================
    Argument      Type    Optional/Required            Notes
    ============  ======  ===========================  ====================================
    **type**      string  required                     photos, collections, users
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
        search = pu.search(type='photos', query='red,car')
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

--------

**PyUnsplash.init_logging(log_level)**
--------------------------------------
    To enable ``logging``, use the ``init_logging`` method.

    **Parameters**

    ============  ======  ====================================  ====================================
    Argument      Type    Optional/Required                     Notes
    ============  ======  ====================================  ====================================
    log_level     number  optional (default: logging.CRITICAL)  Numeric values mapped from ``logging``
                                                                library
    ============  ======  ====================================  ====================================

    **Returns**

    ==========  ========================================================================
    None
    ==========  ========================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        pu.init_logging(logging.DEBUG)

        # use the PyUnsplash objects: all logs will be recorded to log file


