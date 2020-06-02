###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 6/1/2020
#   Purpose: Example file for Search
#
#  Revision: 1
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

search = py_un.search(type_="photos", query="bear")
while search.has_next:
    print(search.link_next, search.link_last)
    search = search.get_next_page()
