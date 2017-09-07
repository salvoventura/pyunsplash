###############################################################################
#
#      File: example_collections.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: Example file for collections
#
#   Comment:
#
###############################################################################
import logging
from pyunsplash import PyUnsplash
api_key = 'YOU_API_KEY'

# instantiate PyUnsplash object
py_un = PyUnsplash(api_key=api_key)

# initiate logging if desired: will automatically create logfile
py_un.init_logging(logging.DEBUG)

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
    photos = collection.photos
    # two ways of iterating: '.body' and '.entries' as well
    for photo in photos.entries:
        print('Photo in collection', photo.id, photo.link_download)


# You can test for navigation links and get a new 'Collections' object
# for the next, previous, first and last pages
if collections_page.has_next:
    collections_page_next = collections_page.get_next_page()

if collections_page.has_previous:
    collections_page_prev = collections_page.get_previous_page()
