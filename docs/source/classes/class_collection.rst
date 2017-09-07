#####################
API: Class Collection
#####################
This class is used to interact with individual ``Collection`` objects typically returned by ``PyUnsplash`` as part of
``Collections`` object entries.


======================
Methods and properties
======================
Methods and properties exposed by the ``Collection`` class.

**Collection.refresh()**
------------------------
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
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            collection.refresh()
            print collection.id


--------

**Collection.id**
-----------------
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
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            print collection.id


--------

**Collection.title**
--------------------
    Title of this collection.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **string**  title of this collection
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            print collection.title


--------

**Collection.description**
--------------------------
    Description for this collection.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **string**  description for this collection
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            print collection.description


--------

**Collection.user**
-------------------
    User who created this collection.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    **string**  id of user who created this collection
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            print collection.user


--------

**Collection.link_photos**
--------------------------
    API location of this collection's photos.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ===================================================
    **string**  url to the API location of this collection's photos
    ==========  ===================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            print collection.link_photos

--------


**Collection.link_related**
---------------------------
    API location of this collection's related collections. (Non-curated collections only)

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ================================================================
    **string**  url to the API location of this collection's related collections
    ==========  ================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            print collection.link_related

--------


**Collection.photos(page, per_page, order_by)**
-----------------------------------------------
    Allows easy access to each photo in this ``Collection``.
    Returns ``Photos`` collection object from this collection's ``link_photos`` url.

    **Parameters**

    ============  ======  ==========================  ====================================
    Argument      Type    Optional/Required           Notes
    ============  ======  ==========================  ====================================
    **page**      number  optional (default: 1)       Page number to retrieve.
    **per_page**  number  optional (default: 10)      Number of items per page (max: 30)
    **order_by**  string  optional (default: latest)  latest, oldest, popular
    ============  ======  ==========================  ====================================

    **Returns**

    ==========  ===================================================
    **Object**  Instance of class ``Photos``
    ==========  ===================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            photos = collection.photos(order_by='popular', per_page=3)
            for photo in photos.entries:
                print photo.id, photo.link_download

--------


**Collection.related()**
------------------------
    Allows easy access to ``Collection``s related to this ``Collection``.
    Returns ``Collections`` object from this collection's ``link_related`` url.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ================================================================
    **Object**  Instance of class ``Collections``
    ==========  ================================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        collections_page = pu.collections(type='featured', per_page=5)
        for collection in collections_page.entries:
            related_collections = collection.related
            for rel_collection in related_collections.entries:
                print rel_collection.title, rel_collection.description


--------



