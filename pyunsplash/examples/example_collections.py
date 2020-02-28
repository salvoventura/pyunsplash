###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_collections.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: Example file for collections
#
#  Revision: 2
#   Comment: What's new in revision 2
#            Add application level logging and interaction with
#            library logging example
#
#   Comment: What's new in revision 1
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

# Get a page from the collections api
# Parameters:
#   'type' : 'generic', 'curated', 'featured'
#            default: 'generic'
#   'page' : <int>, which page to retrieve
#   'per_page': <int>, how many collections to include in each page
#
collections_page = py_un.collections(type_='generic', per_page=3)

# iterate through all the collections retrieved in the collections_page, two ways
# 1) iterating through 'body' returns just a dictionary, no additional API call
for collection in collections_page.body:
    print('Collection as dictionary', collection.get('id'), collection.get('title'))

# 2) iterating through 'entries' returns an instance of 'Collection'
for collection in collections_page.entries:
    print('Collection as object', collection.id, collection.title)

    # a Collection object allows for a richer interaction:
    # follow the 'related' collections, if any
    related_collections = collection.related
    # it's a Collections object too
    for related in related_collections.entries:
        print('Related collection', related.id, related.title)

    # go through all the 'photos' in the collection
    photos = collection.photos()
    # two ways of iterating: '.body' and '.entries' as well
    for photo in photos.entries:
        print('Photo in collection', photo.id, photo.link_download, photo.get_attribution())


# You can test for navigation links and get a new 'Collections' object
# for the next, previous, first and last pages
if collections_page.has_next:
    collections_page_next = collections_page.get_next_page()

if collections_page.has_previous:
    collections_page_prev = collections_page.get_previous_page()
