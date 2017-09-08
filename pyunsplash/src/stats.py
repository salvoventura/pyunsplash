###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: stats.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose: Handle Stats
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .unobject import UnsplashObject


class Stats(UnsplashObject):
    def __init__(self, api_key):
        url = '{}/stats/total'.format(self._api_root)
        super(Stats, self).__init__(source=url, api_key=api_key)

    @property
    def total(self):
        return self.body
