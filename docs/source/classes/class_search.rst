#################
API: Class Search
#################
This class is used to interact with the ``Unsplash`` ``/search/`` REST API.

The constructor is invoked through the main ``PyUnsplash`` class as ``PyUnsplash.search(type, page, per_page, query)``


======================
Methods and properties
======================
Methods and properties exposed by the ``Search`` class.

**Search.entries**
------------------
    Returns an iterator for the returned objects contained in this ``Search`` instance.
    Each entry will be an instance of class ``Collection``, ``Photo`` or ``User`` according
    to the search ``type``.


    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =======================================
    iterator    each time an instance of class ``User``
    ==========  =======================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        search = pu.search(type='photos', query='red,car')
        for photo in search.entries:
            print photo.id, photo.link_download


