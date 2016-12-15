###############################################################################
#
#      File: stats.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose:
#
#   Comment:
#
###############################################################################
import logging
from .unobject import UnsplashObject
from .settings import LIB_NAME

logger = logging.getLogger(LIB_NAME)


class Stats(UnsplashObject):
    def __init__(self, api_key):
        url = '{}/stats/total'.format(self._api_root)
        super(Stats, self).__init__(source=url, api_key=api_key)

    @property
    def total(self):
        return self.body
