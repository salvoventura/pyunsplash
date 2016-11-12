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


class GenericCollection(object):
    # TODO: add way to check what my last_page was in case of paging.
    def __init__(self, api_key):
        self._api_root = 'https://api.unsplash.com'
        self._api_key = api_key
        self.url_self = None
        self.obj_self = None

        self._rest = rest.Rest(api_key=self._api_key)
        self.status_code = None
        self.body = None
        self.headers = None
        self.links = None
        self.navigation = None

    def get_sub_url(self, sub_url, valid_options=None, **kwargs):
        logger.debug('generic get_sub_url {} {} {}'.format(sub_url, valid_options, kwargs))
        if self.url_self is None:
            url = "{}/{}".format(self._api_root.rstrip('/'), sub_url.lstrip('/'))
        else:
            url = "{}/{}".format(self.url_self.rstrip('/'), sub_url.lstrip('/'))
        return self.get_url(url=url, valid_options=valid_options, **kwargs)

    def get_url(self, url, valid_options=None, **kwargs):
        logger.debug('generic get_url {} {} {}'.format(url, valid_options, kwargs))
        query_params = {}
        for key in kwargs:
            if key not in valid_options:
                logger.info('invalid parameter {}, safely ignoring it'.format(key))
                continue
            query_params[key] = kwargs[key]

        self._rest.get(url, query_params=query_params)
        return {
            'status_code': self._rest.status_code,
            'body': self._rest.body,
            'headers': self._rest.headers,
            'links': self._rest.links,
        }

    def reload(self):
        """
        Reload the object from its self url.

        :return: None
        """
        self._rest.get(self.url_self)
        if self._rest.status_code == 200:
            self.obj_self = self._rest.body



    # def load_from_url(self, url):
    #     if url is None:
    #         return False
    #     self._rest.get(url)
    #     if 200 <= self._rest.status_code < 300:
    #         self._cururl = url
    #         self.status_code = self._rest.status_code
    #         self.body = self._rest.body
    #         self.headers = self._rest.headers
    #         self.links = self._rest.links
    #         self.navigation = self._rest.navigation
    #         return True
    #     else:
    #         return False

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


class GenericObject(GenericCollection):
    def __init__(self, api_key, sub_url, source):
        super(GenericObject, self).__init__(api_key)
        self._api_collection = '{}/{}'.format(self._api_root, sub_url.lstrip('/'))

        # guess format based on source type, extract the link to self
        if isinstance(source, dict):
            self_body = source
            self_url = source.get('links').get('self')

        elif isinstance(source, str):
            self_body = None
            if source.startswith(self._api_collection + '/'):
                self_url = source
            elif str(source).isalnum():
                self_url = '{}/{}'.format(self._api_collection, source)
            elif source == sub_url:
                self_url = self._api_collection
            else:
                logger.debug('Source is a string, but we did not handle it: {}'.format(source))
        else:
            logger.info('Invalid parameter to constructor: {}'.format(source))
            raise ValueError('Invalid parameter to constructor: {}')

        # link to self
        self.url_self = self_url
        self.obj_self = self_body
        if self.obj_self is None:
            # need to (re)load
            self.reload()
