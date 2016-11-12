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

from collections import Collection
from generic import GenericObject
from photos import Photo
from users import User

logger = logging.getLogger('pyunsplash')


class Search(GenericObject):
    def __init__(self, api_key):
        super(Search, self).__init__(api_key, '/search', '/search')

    def photos(self, **kwargs):
        """
        Get a single page of photo results for a query.
        Search results limited to 20 photos per page.
        The photo objects returned here are abbreviated. For full details use GET /photos/:id.

        :param query: str - Search terms.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :return:
        """
        sub_url = '/photos'
        valid_options = ['query', 'page']
        response = self.get_sub_url(sub_url, valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def collections(self, **kwargs):
        """
        Get a single page of collection results for a query.
        Search results limited to 20 collections per page.

        :param query: str - Search terms.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :return:
        """
        sub_url = '/collections'
        valid_options = ['query', 'page']
        response = self.get_sub_url(sub_url, valid_options, **kwargs)
        return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def users(self, **kwargs):
        """
        Get a single page of collection results for a query.
        Search results limited to 20 users per page

        :param query: str - Search terms.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :return:
        """
        sub_url = '/users'
        valid_options = ['query', 'page']
        response = self.get_sub_url(sub_url, valid_options, **kwargs)
        return [User(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

