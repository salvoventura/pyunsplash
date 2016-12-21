################
API: Class Users
################
This class is used to interact with lists of ``User`` objects as returned by certain ``unsplash`` REST APIs.

The following class methods/properties in ``PyUnsplash`` return a ``Users`` class object:
  - User.followers()
  - User.following()


======================
Methods and properties
======================
Methods and properties exposed by the ``Users`` class.

**Users.entries**
-------------------------------------
    Returns an iterator for the ``User`` objects contained in this ``Users`` instance

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
        this_user = pu.user('salvoventura', w=100, h=100)
        followers = this_user.followers()    # followers is an instance of class Users
        for user in followers.entries:
            print user.id, user.body.get('first_name'), user.body.get('last_name')


