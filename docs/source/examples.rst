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
