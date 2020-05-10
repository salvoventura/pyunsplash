###############################################################################
#    Copyright (c) 2020 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: example_single_photo.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 5/9/2020
#   Purpose: Example file for SinglePhoto
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

# Get a single photo from a known ID
photo = py_un.photos(type_="single", photo_id='l0_kVknpO2g')
print(photo.entries.get_attribution(format='txt'))
print(photo.entries.get_attribution(format='html'))


