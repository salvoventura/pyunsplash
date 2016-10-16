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

import _generic

logger = logging.getLogger('pyunsplash')


class Collections(_generic.Generic):
    def __init__(self):
        super(Collections, self).__init__('/collections')

    def get(self, id_):
        """
        Retrieve a single collection.
        To view a user's private collections, the read_collections scope is required.

        :param id_: str - The collections's ID. Required.
        :return:
        """
        url_ = self._sanitized_url(id_)
        self._loadurl(url_)
        return self.body

    def get_related(self, id_):
        """
        Retrieve a list of collections related to this one.

        :param id_: str - The collections's ID. Required.
        :return:
        """
        url_ = self._sanitized_url(str(id_) + '/related')
        self._loadurl(url_)
        return self.body

    def get_all(self, **kwargs):
        """
        Get a single page from the list of all collections.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        url_ = self._sanitized_url('')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    def get_all_featured(self, **kwargs):
        """
        Get a single page from the list of featured collections.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        url_ = self._sanitized_url('/featured')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    def get_all_curated(self, **kwargs):
        """
        Get a single page from the list of curated collections.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        url_ = self._sanitized_url('/curated')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    def get_photos(self, id_, **kwargs):
        """
        Retrieve a collection's photos.

        :param id_: str - The collection's ID. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        url_ = self._sanitized_url(str(id_) + '/photos')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    def get_curated_photos(self, id_, **kwargs):
        """
        Retrieve a curated collection's photos.

        :param id_: str - The collection's ID. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        url_ = self._sanitized_url('/curated/' + str(id_) + '/photos')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    # TODO: POST /collections
    # TODO: PUT /collections/:id
    # TODO: DELETE /collections/:id
    # TODO: POST /collections/:collection_id/add
    # TODO: DELETE /collections/:collection_id/remove
