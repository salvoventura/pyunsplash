###############################################################################
#
#      File: pyunsplash.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose: simplify import statements
#
#   Comment:
#
###############################################################################
from pyunsplash import PyUnsplash
import os
# TRAVIS_BUILD_NUMBER
# TRAVIS_COMMIT
# TRAVIS_COMMIT_RANGE
# TRAVIS_TAG
__version__ = '1.0.0a1'
__build__ = '{}({})'.format(__version__, os.environ('TRAVIS_BUILD_NUMBER'))
