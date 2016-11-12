###############################################################################
#
#      File: stats.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 15 Oct 2016
#   Purpose: Interface to /stats
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

from generic import GenericObject

logger = logging.getLogger('pyunsplash')


class Stats(GenericObject):
    def __init__(self, api_key):
        super(Stats, self).__init__(api_key, '/stats', '/stats')

    def get_total(self):
        """
        Get a list of counts for all of Unsplash.

        :return:
        """
        url_ = self._sanitized_url('/total')
        self._loadurl(url_)
        return self.body
