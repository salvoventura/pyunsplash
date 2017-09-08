###############################################################################
#    Copyright (c) 2017 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: liblogging.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 07 Sep 2017
#   Purpose: Centralize module logging
#
#  Revision: 1
#   Comment: At the module level pyunsplash defines a logger called via LIB_NAME
#            called in this case "pyunsplash".
#            As per best practice, it is off by default, and can be tuned directly
#            by using getLogger/setLevel from the application layer.
#            See examples for this.
#
###############################################################################
import logging
from .settings import LIB_NAME, LOG_LEVEL
logger = logging.getLogger(LIB_NAME)
logger.addHandler(logging.NullHandler())
logger.setLevel(LOG_LEVEL)
