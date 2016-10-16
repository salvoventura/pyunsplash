###############################################################################
#
#      File: search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 15 Oct 2016
#   Purpose: Interface to /search
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

import generic

logger = logging.getLogger('pyunsplash')


class Search(generic.Generic):
    def __init__(self, api_key):
        super(Search, self).__init__(api_key, '/search')

    def photos(self, **kwargs):
        """
        Get a single page of photo results for a query.
        Search results limited to 20 photos per page.
        The photo objects returned here are abbreviated. For full details use GET /photos/:id.

        :param query: str - Search terms.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :return:
        """
        url_ = self._sanitized_url('/photos')
        valid_options = ['query', 'page']
        return self._get(url_, valid_options, **kwargs)

    def collections(self, **kwargs):
        """
        Get a single page of collection results for a query.
        Search results limited to 20 collections per page.

        :param query: str - Search terms.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :return:
        """
        url_ = self._sanitized_url('/collections')
        valid_options = ['query', 'page']
        return self._get(url_, valid_options, **kwargs)

    def users(self, **kwargs):
        """
        Get a single page of collection results for a query.
        Search results limited to 20 users per page

        :param query: str - Search terms.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :return:
        """
        url_ = self._sanitized_url('/users')
        valid_options = ['query', 'page']
        return self._get(url_, valid_options, **kwargs)

