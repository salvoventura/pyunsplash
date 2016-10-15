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

import generic

logger = logging.getLogger('pyunsplash')


class Stats(generic.Generic):
    def __init__(self):
        super(Stats, self).__init__('/stats')

    def get_total(self):
        """
        Get a list of counts for all of Unsplash.

        :return:
        """
        url_ = self._sanitized_url('/total')
        self._loadurl(url_)
        return self.body
