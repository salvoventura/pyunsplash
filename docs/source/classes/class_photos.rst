#################
API: Class Photos
#################
This class is used to interact with the ``Unsplash`` ``/photos`` REST API but also with lists of ``Photo`` objects
as returned by certain ``unsplash`` REST APIs.

The constructor can be invoked through the main ``PyUnsplash`` class as ``PyUnsplash.photos(type, page, per_page, order_by)``.

The following class methods/properties in ``PyUnsplash`` also return a ``Photos`` class object:
  - User.likes(page, per_page, order_by)
  - User.photos(page, per_page, order_by)


======================
Methods and properties
======================
Methods and properties exposed by the ``Photos`` class.

**Photos.entries**
------------------
    Returns an iterator for the ``Photo`` objects contained in this ``Photos`` instance

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ========================================
    iterator    each time an instance of class ``Photo``
    ==========  ========================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        photos = this_user.photos()    # photos is an instance of class Photos
        for photo in photos.entries:
            print photo.id, photo.link_download

