###############################################################################
#
#      File: users.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 13 Oct 2016
#   Purpose: Interface to /users
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

from collections import Collection
from generic import GenericCollection, GenericObject
from photos import Photo

logger = logging.getLogger('pyunsplash')


class Users(GenericCollection):
    def __init__(self, api_key):
        super(Users, self).__init__(api_key)

    def get(self, source):
        """
        Return a user object based on source

        :param source: username, url or json body
        :return:
        """
        return User(self._api_key, source)


class User(GenericObject):
    def __init__(self, api_key, source):
        super(User, self).__init__(api_key, '/users', source)

    def get(self, **kwargs):
        """
        Retrieve public details on a given user.
        Supplying the optional w or h parameters will result in the custom photo
        URL being added to the profile_image object.

        :param w: int - Profile image width in pixels. Optional.
        :param h: int - Profile image height in pixels. Optional.
        :return:
        """
        url = self.url_self
        valid_options = ['w', 'h']
        response = self.get_url(url, valid_options, **kwargs)
        if response.get('status_code') == 200:
            self.obj_self = response.get('body')
            return self.obj_self

    def get_portfolio(self):
        """
        Retrieve this user's portfolio link.

        :return: str, url
        """
        sub_url = '/portfolio'
        response = self.get_url(sub_url)
        if response.get('status_code') == 200:
            return response.get('body')

    def get_following(self, **kwargs):
        """
        API location of users this user is following.

        :param username: str - The user's username. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        # TODO: test and verify is paging is supported
        sub_url = '/following'
        valid_options = ['page', 'per_page']
        response = self.get_url(sub_url, valid_options)
        if response.get('status_code') == 200:
            return response.get('body')

    def get_followers(self, **kwargs):
        """
        API location of this user's followers.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        # TODO: test and verify is paging is supported
        sub_url = '/followers'
        valid_options = ['page', 'per_page']
        response = self.get_url(sub_url, valid_options)
        if response.get('status_code') == 200:
            return response.get('body')

    def get_photos(self, **kwargs):
        """
        Get a list of photos uploaded by a user.
        The photo objects returned here are abbreviated.
        For full details use GET /photos/:id

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :param order_by: str - How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return:
        """
        sub_url = '/photos'
        valid_options = ['page', 'per_page', 'order_by']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if
                response.get('status_code') == 200]

    def get_likes(self, **kwargs):
        """
        Get a list of photos liked by this user.
        The photo objects returned here are abbreviated.
        For full details use GET /photos/:id

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :param order_by: str - How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return:
        """
        sub_url = '/likes'
        valid_options = ['page', 'per_page', 'order_by']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if
                response.get('status_code') == 200]

    def get_collections(self, **kwargs):
        """
        Get a list of collections created by this user.

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        sub_url = '/collections'
        valid_options = ['page', 'per_page']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Collection(self._api_key, source) for source in response.get('body') if
                response.get('status_code') == 200]


