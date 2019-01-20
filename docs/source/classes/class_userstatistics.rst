#########################
API: Class UserStatistics
#########################
This class is used to interact with the ``Unsplash`` ``/users/:username/statistics`` REST API.

The constructor is invoked through the ``PyUnsplash.User`` class as ``PyUnsplash.User.statistics()``


======================
Methods and properties
======================
Methods and properties exposed by the ``UserStatistics`` class.

**UserStatistics.downloads**
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
    **dict**    Dictionary containing statistic data from `downloads`
    ==========  =====================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura')
        user_statistics = this_user.statistics()
        print (user_statistics.downloads.get('total'))
        print (user_statistics.downloads.get('historical', {}).get('change', None))

--------

**UserStatistics.views**
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
    **dict**    Dictionary containing statistic data from `views`
    ==========  =====================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura')
        user_statistics = this_user.statistics()
        print (user_statistics.views.get('total'))
        print (user_statistics.views.get('historical', {}).get('change', None))

--------

**UserStatistics.likes**
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
    **dict**    Dictionary containing statistic data from `likes`
    ==========  =====================================================

    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        this_user = pu.user('salvoventura')
        user_statistics = this_user.statistics()
        print (user_statistics.likes.get('total'))
        print (user_statistics.likes.get('historical', {}).get('change', None))

