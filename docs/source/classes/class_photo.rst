################
API: Class Photo
################
This class is used to interact with individual ``Photo`` objects typically returned by ``PyUnsplash`` as part of ``Photos``
object entries.


======================
Methods and properties
======================
Methods and properties exposed by the ``Photo`` class.

**Photo.refresh()**
-------------------
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
        photos = this_user.photos()    # photos is an instance of class Photos
        for photo in photos.entries:
            photo.refresh()
            print photo.id, photo.link_download


--------

**Photo.id**
------------
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
        photos = this_user.photos()    # photos is an instance of class Photos
        for photo in photos.entries:
            photo.refresh()
            print photo.id, photo.link_download


--------

**Photo.link_html**
-------------------
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
        photos = this_user.photos()    # photos is an instance of class Photos
        for photo in photos.entries:
            print photo.id, photo.link_html

--------

**Photo.link_download**
-----------------------
    Download location of this resource.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ==============================================
    **string**  url to the download location of the resource
    ==========  ==============================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        photos = this_user.photos()    # photos is an instance of class Photos
        for photo in photos.entries:
            print photo.id, photo.link_download

--------

**User.stats**
-----------------------
    Retrieve a single photo's stats.

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  ================================================
    **json**    JSON encoded stats information about this photo
    ==========  ================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura', w=100, h=100)
        photos = this_user.photos()    # photos is an instance of class Photos
        for photo in photos.entries:
            print photo.stats

