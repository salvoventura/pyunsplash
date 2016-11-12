###############################################################################
#
#      File: collections.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 15 Oct 2016
#   Purpose: Interface to /collections
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

from generic import GenericCollection, GenericObject
from photos import Photo

logger = logging.getLogger('pyunsplash')


class Collections(GenericCollection):
    def __init__(self, api_key):
        super(Collections, self).__init__(api_key)

    def get(self, source):
        """
        Return a collection object based on source

        :param source: collection id, url or json body
        :return:
        """
        return Collection(self._api_key, source=source)

    def get_all(self, **kwargs):
        """
        Get a single page from the list of all collections.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        sub_url = '/collections'
        valid_options = ['page', 'per_page']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_featured(self, **kwargs):
        """
        Get a single page from the list of featured collections.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        sub_url = '/collections/featured'
        valid_options = ['page', 'per_page']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_curated(self, **kwargs):
        """
        Get a single page from the list of curated collections.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        sub_url = '/collections/curated'
        valid_options = ['page', 'per_page']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_next(self):
        """
        Retrieve next page from last call query and return
        list of Collections

        :return:
        """
        if self.navigation.get('next') is not None:
            response = self.get_url(self.navigation.get('next'))
            return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_previous(self):
        """
        Retrieve previous page from last call query and return
        list of Collections

        :return:
        """
        if self.navigation.get('prev') is not None:
            response = self.get_url(self.navigation.get('prev'))
            return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    # TODO: POST /collections
    # TODO: PUT /collections/:id
    # TODO: DELETE /collections/:id
    # TODO: POST /collections/:collection_id/add
    # TODO: DELETE /collections/:collection_id/remove


class Collection(GenericObject):
    def __init__(self, api_key, source):
        super(Collection, self).__init__(api_key, '/collections', source)

    def get_related(self):
        """
        Retrieve a list of collections related to this one.

        :return:
        """
        sub_url = '/related'
        response = self.get_url(sub_url)
        return [Collection(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_photos(self, **kwargs):
        """
        Retrieve this collection's photos.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        valid_options = ['page', 'per_page']
        response = self.get_url(self.url_self + '/photos', valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_curated_photos(self, **kwargs):
        """
        Retrieve this curated collection's photos.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        # This is the same as above: effectively we might remove this method
        # as it only applies to curated collections... In other words, if the
        # collection is curated, self.url_self is already correct
        valid_options = ['page', 'per_page']
        response = self.get_url(self.url_self + '/photos', valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]













































