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

from generic import GenericCollection, GenericObject

logger = logging.getLogger('pyunsplash')


class Photos(GenericCollection):
    def __init__(self, api_key):
        super(Photos, self).__init__(api_key)

    def get(self, source):
        """
        Return a photo object based on source

        :param source: collection id, url or json body
        :return:
        """
        return Photo(self._api_key, source=source)

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
        sub_url = '/photos'
        valid_options = ['page', 'per_page', 'order_by']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

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
        sub_url = '/photos/curated'
        valid_options = ['page', 'per_page', 'order_by']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

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
        sub_url = '/photos/random'
        valid_options = ['category', 'collections', 'featured', 'username', 'query', 'w', 'h', 'orientation', 'count']
        response = self.get_url(sub_url, valid_options, **kwargs)
        return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_next(self):
        """
        Retrieve next page from last call query and return
        list of Photo objects

        :return:
        """
        if self.navigation.get('next') is not None:
            response = self.get_url(self.navigation.get('next'))
            return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    def get_previous(self):
        """
        Retrieve previous page from last call query and return
        list of Photo objects

        :return:
        """
        if self.navigation.get('prev') is not None:
            response = self.get_url(self.navigation.get('prev'))
            return [Photo(self._api_key, source) for source in response.get('body') if response.get('status_code') == 200]

    # TODO: PUT /photos/:id
    # TODO: POST /photos/:id/like
    # TODO: DELETE /photos/:id/like


class Photo(GenericObject):
    def __init__(self, api_key, source, **kwargs):
        super(Photo, self).__init__(api_key, '/photos', source)

    def get(self, **kwargs):
        """
        Reload this photo, allows for optional parameters.
        Supplying the optional w or h parameters will result in the custom photo URL being added to the urls object.

        :param w: int - Image width in pixels. Optional.
        :param h: int - Image height in pixels. Optional.
        :param rect: dict - dictionary of 4 integers representing x, y, width, height of the cropped rectangle.
                     {'x': 0, 'y': 0, 'w': 100, 'h': 100}
        :return:
        """
        url = self.url_self
        valid_options = ['w', 'h', 'rect']
        response = self.get_url(url, valid_options, **kwargs)
        if response.get('status_code') == 200:
            self.obj_self = response.get('body')
            return self.obj_self

    def get_stats(self):
        """
        Retrieve this photo's stats.
        Views are currently updated once daily.

        :return:
        """
        sub_url = '/stats'
        response = self.get_url(sub_url)
        if response.get('status_code') == 200:
            return response.get('body')

    def get_download(self):
        """
        Retrieve this photo's download link.
        Preferably hit this endpoint if a photo is downloaded in your application for use
        (example: to be displayed on a blog article, to be shared on social media, to be remixed, etc.).
        This is different than the concept of a view, which is tracked automatically when you hotlinking an image

        :return:
        """
        sub_url = '/download'
        response = self.get_url(sub_url)
        if response.get('status_code') == 200:
            return response.get('body')





