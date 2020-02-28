##########
PyUnsplash
##########
|Latest Version| |Docs Build Status| |Build Status| |Code Coverage| |Code Climate| |Landscape Io| |Say Thanks|

An open source Python wrapper for the `Unsplash REST API <https://unsplash.com/developers>`_.
The source code is available on GitHub at `https://github.com/salvoventura/pyunsplash <https://github.com/salvoventura/pyunsplash>`_.


############
Installation
############
``PyUnsplash`` is available on `PyPI <https://pypi.python.org/pypi>`_ and thus can be installed with ``pip`` on most platforms.
::

    $ pip install pyunsplash

############
Dependencies
############
This library depends on `Requests <http://docs.python-requests.org>`_ to make - well - requests to the Unsplash API.
This additional package should be automatically installed at installation time, or you can simply install it by:
::

    $ pip install requests

########
Examples
########
This example shows how the interaction with the paging functionality of the unsplash API is greatly abstracted and
simplified. The code below will iterate through all collections, and retrieve each photo in there, and print their
download link.

.. code-block:: python

    import logging
    from pyunsplash import PyUnsplash
    api_key = 'YOUR_APPLICATION_ID'

    # instantiate PyUnsplash object
    py_un = PyUnsplash(api_key=api_key)

    # pyunsplash logger defaults to level logging.ERROR
    # If you need to change that, use getLogger/setLevel
    # on the module logger, like this:
    logging.getLogger("pyunsplash").setLevel(logging.DEBUG)

    # Start with the generic collection, maximize number of items
    # note: this will run until all photos of all collections have
    #       been visited, unless a connection error occurs.
    #       Typically the API hourly limit gets hit during this
    #
    collections = py_un.collections(per_page=30)
    while collections.has_next:
        for collection in collections.entries:
            photos = collection.photos()
            for photo in photos.entries:
                print collection.title, photo.link_download, photo.get_attribution()

        # no need to specify per_page: will take from original object
        collections = collections.get_next_page()

#############
Documentation
#############
Documentation is published on `ReadTheDocs <http://pyunsplash.readthedocs.io/>`_.


#######
Version
#######
**PyUnsplash v1.0.0b9 (beta, v9)**

    - Introduce `get_attribution` method in class Photo
    - Update tests, examples and documentation accordingly
    - Update documentation for objects supporting `.body` attribute
    - Update Copyright years adding 2020

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b8 (beta, v8)**

    - Fix documentation for random photos API endpoint
    - Update library and documentation for deprecated 'curated' photos
    - Update library and documentation for deprecated 'curated' collection
    - Add library warning in logs for 'curated' when used
    - Fix documentation for object parameter ``type_`` instead of ``type``
    - Core library now raising exception for invalid parameters
    - Added support for user statistics API, and related doc and tests

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b7 (beta, v7)**

    Fixed issues submitted on GitHub:
    - Search class: Param "type" is "type_"
    - Provide property for `download_location` in PyUnsplasy.Photo class

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b6 (beta, v6)**

    Added Python3 support

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b5 (beta, v5)**

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b4 (beta, v4)**

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b3 (beta, v3)**

    Still troubles in getting Travis-Ci and PyPI publishing automation tied.

    **Todo**
    - Get `PyPI <https://pypi.python.org/pypi/pyunsplash/>`_ publishing automated via `Travis-Ci <https://travis-ci.org/salvoventura/pyunsplash/>`_ after tag commits.
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b2 (beta, v2)**

    Getting Travis-Ci and PyPI publishing automation tied.

    **Todo**
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0b1 (beta, v1)**

    Logging subsystem overhaul, now cleaner. Changes have percolated across many files.
    Documentation checked and verified, and issues fixed.

    **Todo**
    - Get `PyPI <https://pypi.python.org/pypi/pyunsplash/>`_ publishing automated via
        `Travis-Ci <https://travis-ci.org/salvoventura/pyunsplash/>`_ after tag commits.
    - Authorization workflow & Current user
    - Write operations


--------

**PyUnsplash v1.0.0a3 (alpha, v3)**

    v1.0.0a2 broke the library with the attempt to import the build number from Travis via the environment variable,
    which obviously vanishes outside of the CI system. Fixed. Will need a different solution if I really want/need
    build numbering inside the library version number.

    **Todo**
        Still struggling to get `PyPI <https://pypi.python.org/pypi/pyunsplash/>`_ publishing automated via
        `Travis-Ci <https://travis-ci.org/salvoventura/pyunsplash/>`_ after tag commits.

--------

**PyUnsplash v1.0.0a2 (alpha, v2)**

    Added support and integration for more tools, which also required some code cleanup:

    - integrate and run automated unit tests
    - integrate with CodeCov
    - integrate with CodeClimate

    **Todo**
        Still struggling to get PyPI publishing automated via Travis-Ci after tag commits.

--------

**PyUnsplash v1.0.0a1 (alpha, v1)**

    This first release offers read-only capabilities to the `Unsplash REST API <https://unsplash.com/documentation/>`_.
    Although with this limitation, I thought it would be useful to start exposing the library and collect
    feedback from the community early on.

    Features that are right now on my TODO list:

    - Authorization workflow & Current user
    - Write operations

    Desired:
        - More unit-test coverage
        - Documentation review


#######
License
#######
PyUnsplash is released under the `MIT License <http://www.opensource.org/licenses/MIT>`_.


.. |Build Status| image:: https://travis-ci.org/salvoventura/pyunsplash.svg?branch=master
    :target: https://travis-ci.org/salvoventura/pyunsplash
    :alt: Build Status

.. |Docs Build Status| image:: https://readthedocs.org/projects/pyunsplash/badge/?version=latest
    :target: http://pyunsplash.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |Latest Version| image:: https://badge.fury.io/py/pyunsplash.svg
    :target: https://badge.fury.io/py/pyunsplash

.. |Code Coverage| image:: https://codecov.io/gh/salvoventura/pyunsplash/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/salvoventura/pyunsplash

.. |Code Climate| image:: https://codeclimate.com/github/salvoventura/pyunsplash/badges/gpa.svg
   :target: https://codeclimate.com/github/salvoventura/pyunsplash
   :alt: Code Climate

.. |Landscape Io| image:: https://landscape.io/github/salvoventura/pyunsplash/master/landscape.svg?style=flat
   :target: https://landscape.io/github/salvoventura/pyunsplash/master
   :alt: Code Health

.. |Say Thanks| image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
   :target: https://saythanks.io/to/salvoventura
   :alt: Say Thanks
