######################
API: Class Collections
######################
This class is used to interact with the ``Unsplash`` ``/collections`` REST API but also with lists of ``Collection`` objects
as returned by certain ``unsplash`` REST APIs.

The constructor can be invoked through the main ``PyUnsplash`` class as ``PyUnsplash.collections(type, page, per_page)``.

The following class methods/properties in ``PyUnsplash`` also return a ``Collections`` class object:
  - Collection.related()
  - User.collections(page, per_page, order_by)


======================
Methods and properties
======================
Methods and properties exposed by the ``Collections`` class.

**Collections.entries**
-----------------------
    Returns an iterator for the ``Collection`` objects contained in this ``Collections`` instance

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =============================================
    iterator    each time an instance of class ``Collection``
    ==========  =============================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        collections = this_user.collections(page=1, per_page=5)
        for collection in collections.entries:
            print collection.id, collection.title

