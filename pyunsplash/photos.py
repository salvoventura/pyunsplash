###############################################################################
#
#      File: photos.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Oct 2016
#   Purpose: Interface to /photos
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

import generic

logger = logging.getLogger('pyunsplash')


class Photos(generic.Generic):
    def __init__(self):
        super(Photos, self).__init__('/photos')

    def get(self, id_, **kwargs):
        """
        Retrieve a single photo.
        Supplying the optional w or h parameters will result in the custom photo URL being added to the urls object.

        :param id_: str - The photo's ID. Required.
        :param w: int - Image width in pixels. Optional.
        :param rect: dict - dictionary of 4 integers representing x, y, width, height of the cropped rectangle.
                     {'x': 0, 'y': 0, 'w': 100, 'h': 100}
        :return:
        """
        url_ = self._sanitized_url(id_)
        valid_options = ['w', 'h', 'rect']
        return self._get(url_, valid_options, **kwargs)

    def get_stats(self, id_):
        """
        Retrieve a single photo's stats.
        Views are currently updated once daily.

        :param id_: str - The photo's ID. Required.
        :return:
        """
        url_ = self._sanitized_url(str(id_) + '/stats')
        self._loadurl(url_)
        return self.body

    def get_download(self, id_):
        """
        Retrieve a single photo's stats.
        Views are currently updated once daily.

        :param id_: str - The photo's ID. Required.
        :return:
        """
        url_ = self._sanitized_url(str(id_) + '/download')
        self._loadurl(url_)
        return self.body

    def get_all(self, **kwargs):
        """
        Get a single page from the list of all photos.
        The photo objects returned here are abbreviated.
        For full details use GET /photos/:id

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :param order_by: str - How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return:
        """
        url_ = self._sanitized_url('')
        valid_options = ['page', 'per_page', 'order_by']
        return self._get(url_, valid_options, **kwargs)

    def get_curated(self, **kwargs):
        """
        Get a single page from the list of the curated photos (front-page's photos).
        The photo objects returned here are abbreviated.
        For full details use GET /photos/:id

        :param page: int - Page number to retrieve. (Optional; default: 1)
        :param per_page: int - Number of items per page. (Optional; default: 10)
        :param order_by: str - How to sort the photos. Optional. (Valid values: latest, oldest, popular; default: latest)
        :return:
        """
        url_ = self._sanitized_url('/curated')
        valid_options = ['page', 'per_page', 'order_by']
        return self._get(url_, valid_options, **kwargs)

    def get_random(self, **kwargs):
        """
        Retrieve a single random photo, given optional filters.

        If supplying multiple category ID's, the resulting photos will be those that match all of the given categories,
        not ones that match any category.

        You can't use the collections and query parameters in the same request

        When supplying a count parameter - and only then - the response will be an array of photos,
        even if the value of count is 1.

        :param category: Category ID('s) to filter selection. If multiple, comma-separated. (deprecated)
        :param collections: Public collection ID('s) to filter selection. If multiple, comma-separated.
        :param featured: Limit selection to featured photos.
        :param username: Limit selection to a single user.
        :param query: Limit selection to photos matching a search term.
        :param w: Image width in pixels.
        :param h: Image width in pixels.
        :param orientation: Filter search results by photo orientation. Valid values are landscape, portrait, and squarish.
        :param count: The number of photos to return. (Default: 1; max: 30)
        :return:
        """
        # TODO: test/understand the 'featured' case, is it just a flag, and do i need to handle it differently?
        url_ = self._sanitized_url('/random')
        valid_options = ['category', 'collections', 'featured', 'username', 'query', 'w', 'h', 'orientation', 'count']
        return self._get(url_, valid_options, **kwargs)

    # TODO: PUT /photos/:id
    # TODO: POST /photos/:id/like
    # TODO: DELETE /photos/:id/like
