###############################################################################
#
#      File: example_iteration.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: How to get to every photo in every collection
#
#   Comment: Meant to show the use of the different objects
#            To get every photo, you could just use Photos
#
###############################################################################
import logging
from pyunsplash import PyUnsplash
api_key = 'YOU_API_KEY'

# instantiate PyUnsplash object
py_un = PyUnsplash(api_key=api_key)

# initiate logging if desired: will automatically create logfile
py_un.init_logging(logging.DEBUG)


# Start with the generic collection, maximize number of items
# note: this will run until all photos of all collections have
#       been visited, unless a connection error occurs.
#       Typically the API hourly limit gets hit during this
#
collections = py_un.collections(per_page=30)
while collections.has_next:
    for collection in collections.entries:
        photos = collection.photos
        for photo in photos.entries:
            print(collection.title, photo.link_download)

    # no need to specify per_page: will take from original object
    collections = collections.get_next_page()
