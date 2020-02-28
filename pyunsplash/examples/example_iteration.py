###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_iteration.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: How to get to every photo in every collection
#
#  Revision: 2
#   Comment: What's new in revision 2
#            Add application level logging and interaction with
#            library logging example
#
#   Comment: What's new in revision 1
#            Show the use of the different objects
#            To get every photo, you could just use Photos
#
#
###############################################################################
import logging
import os
from pyunsplash import PyUnsplash
api_key = os.environ.get('APPLICATION_ID', None) or 'DUMMY_APPLICATION_ID'


# Initialize app logging
logger = logging.getLogger()
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# pyunsplash logger defaults to level logging.ERROR
# If you need to change that, use getLogger/setLevel
# on the module logger, like this:
logging.getLogger(PyUnsplash.logger_name).setLevel(logging.DEBUG)


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
            print(collection.title, photo.link_download, photo.get_attribution())

    # no need to specify per_page: will take from original object
    collections = collections.get_next_page()
