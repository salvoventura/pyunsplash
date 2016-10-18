###############################################################################
#
#      File: generic.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 11 Oct 2016
#   Purpose: Base class other inherit from
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

import rest

logger = logging.getLogger('pyunsplash')

# TODO: add way to check what my last_page was in case of paging.
class Generic(object):
    def __init__(self, api_key, collection):
        self._apiurl = 'https://api.unsplash.com'
        self._api_key = api_key
        self._objurl = self._apiurl + '{}'.format(collection)
        self._cururl = self._objurl
        self._rest = rest.Rest(api_key=self._api_key)
        self.status_code = None
        self.body = None
        self.headers = None
        self.links = None
        self.navigation = None

    def _sanitized_url(self, sub_url):
        # sub_url always relative to _objurl if partial
        if str(sub_url).startswith(self._objurl):
            return str(sub_url)
        return self._objurl + '/' + str(sub_url).lstrip('/')

    def _loadurl(self, url_, query_params=None):
        if url_ is None:
            return False
        url = self._sanitized_url(url_)
        self._rest.get(url, query_params=query_params)
        if 200 <= self._rest.status_code < 300:
            self._cururl = url
            self.status_code = self._rest.status_code
            self.body = self._rest.body
            self.headers = self._rest.headers
            self.links = self._rest.links
            self.navigation = self._rest.navigation
            return True
        else:
            return False

    @property
    def has_next(self):
        if self.navigation:
            return self.navigation.get('next') is not None
        return False

    @property
    def has_previous(self):
        if self.navigation:
            return self.navigation.get('prev') is not None
        return False

    def _get(self, url, valid_options, **kwargs):
        query_params = {}
        for key in kwargs:
            if key not in valid_options:
                logger.info('invalid parameter {}, safely ignoring it'.format(key))
                continue
            query_params[key] = kwargs[key]
        self._loadurl(url, query_params=query_params)
        return self.body

    def get_next(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'next' page from the same.

        :return:
        """
        if self.navigation:
            url = self.navigation.get('next')
            if self._loadurl(url):
                return self.body
        return False

    def get_previous(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'previous' page from the same.

        :return:
        """
        if self.navigation:
            url = self.navigation.get('prev')
            if self._loadurl(url):
                return self.body
        return False

    def get_first(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'first' page from the same.

        :return:
        """
        if self.navigation:
            url = self.navigation.get('first')
            if self._loadurl(url):
                return self.body
        return False

    def get_last(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'last' page from the same.

        :return:
        """
        if self.navigation:
            url = self.navigation.get('last')
            if self._loadurl(url):
                return self.body
        return False

    def reset(self):
        """
        Reset the last visited url to the base object url.
        Basically like a fresh instance of this object.

        :return: None
        """
        self._cururl = self._objurl

    def reload(self):
        """
        Reload the last successfully visited url.

        :return: None
        """
        self._load(self._cururl)


