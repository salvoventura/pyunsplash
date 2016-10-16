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

import _generic

logger = logging.getLogger('pyunsplash')


class Users(_generic.Generic):
    def __init__(self):
        super(Users, self).__init__('/users')

    def get(self, username, **kwargs):
        """
        Retrieve public details on a given user.
        Supplying the optional w or h parameters will result in the custom photo
        URL being added to the profile_image object.

        :param username: str - The user's username. Required.
        :param w: int - Profile image width in pixels. Optional.
        :param h: int - Profile image height in pixels. Optional.
        :return:
        """
        url_ = self._sanitized_url(username)
        valid_options = ['w', 'h']
        return self._get(url_, valid_options, **kwargs)

    def get_portfolio(self, username):
        """
        Retrieve a single user's portfolio link.

        :param username: str - The user's username. Required.
        :return: str, url
        """
        url_ = self._sanitized_url(username + '/portfolio')
        self._loadurl(url_)
        return self.body

    def get_following(self, username, **kwargs):
        """
        Get a list of users following the given user.

        :param username: str - The user's username. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        # TODO: test and verify is paging is supported
        url_ = self._sanitized_url(username + '/following')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    def get_followers(self, username, **kwargs):
        """
        Get a list of users followed by the given user.

        :param username: str - The user's username. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        # TODO: test and verify is paging is supported
        url_ = self._sanitized_url(username + '/followers')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)

    def get_photos(self, username, **kwargs):
        """
        Get a list of photos uploaded by a user.
        The photo objects returned here are abbreviated.
        For full details use GET /photos/:id

        :param username: str - The user's username. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :param order_by: str - How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return:
        """
        url_ = self._sanitized_url(username + '/photos')
        valid_options = ['page', 'per_page', 'order_by']
        return self._get(url_, valid_options, **kwargs)

    def get_likes(self, username, **kwargs):
        """
        Get a list of photos liked by a user.
        The photo objects returned here are abbreviated.
        For full details use GET /photos/:id

        :param username: str - The user's username. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :param order_by: str - How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return:
        """
        url_ = self._sanitized_url(username + '/likes')
        valid_options = ['page', 'per_page', 'order_by']
        return self._get(url_, valid_options, **kwargs)

    def get_collections(self, username, **kwargs):
        """
        Get a list of collections created by the user.

        :param username: str - The user's username. Required.
        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :return:
        """
        url_ = self._sanitized_url(username + '/likes')
        valid_options = ['page', 'per_page']
        return self._get(url_, valid_options, **kwargs)









