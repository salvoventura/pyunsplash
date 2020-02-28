################
API: Class Stats
################
This class is used to interact with the ``Unsplash`` ``/stats/total`` REST API.

The constructor is invoked through the main ``PyUnsplash`` class as ``PyUnsplash.stats()``


======================
Methods and properties
======================
Methods and properties exposed by the ``Stats`` class.

**Stats.total**
-------------------------------------
    Description

    **Parameters**

    ============  ======  ========================  ====================================
    Argument      Type    Optional/Required         Notes
    ============  ======  ========================  ====================================
    N/A
    ============  ======  ========================  ====================================

    **Returns**

    ==========  =====================================================
    **json**    JSON encoded stats information about ``Unsplash.com``
    ==========  =====================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        stats = pu.stats()
        print stats.total


--------

**Stats.body**
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
    **string**  Stats object returned by API, in JSON format
    ==========  ============================================
