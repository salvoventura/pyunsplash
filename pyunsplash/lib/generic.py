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
    def __init__(self, api_key):
        self._api_root = 'https://api.unsplash.com'
        self._api_key = api_key
        self.url_self = None
        self.obj_self = None

        self._rest = rest.Rest(api_key=self._api_key)
        self.navigation = None

    def get_url(self, url, valid_options=None, **kwargs):
        logger.debug('generic get_url {} {} {}'.format(url, valid_options, kwargs))

        if not url.startswith('http') and url.find('?') == -1:
            # sub url
            if self.url_self is None:
                url = "{}/{}".format(self._api_root.rstrip('/'), url.lstrip('/'))
            else:
                url = "{}/{}".format(self.url_self.rstrip('/'), url.lstrip('/'))

        query_params = {}
        for key in kwargs:
            if key not in valid_options:
                logger.info('invalid parameter {}, safely ignoring it'.format(key))
                continue
            query_params[key] = kwargs[key]

        self._rest.get(url, query_params=query_params)
        self.navigation = self._rest.navigation
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
        logger.debug('self reloading at {}'.format(self.url_self))
        self._rest.get(self.url_self)
        if self._rest.status_code == 200:
            self.obj_self = self._rest.body

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
        if self.navigation and self.navigation.get('next'):
            self.url_self = self.navigation.get('next')
            self.reload()
        return False

    def get_previous(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'previous' page from the same.

        :return:
        """
        if self.navigation and self.navigation.get('prev'):
            self.url_self = self.navigation.get('prev')
            self.reload()
        return False

    def get_first(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'first' page from the same.

        :return:
        """
        if self.navigation and self.navigation.get('first'):
            self.url_self = self.navigation.get('first')
            self.reload()
        return False

    def get_last(self):
        """
        If the last object retrieved supported pagination,
        this will retrieve the 'last' page from the same.

        :return:
        """
        if self.navigation and self.navigation.get('last'):
            self.url_self = self.navigation.get('last')
            self.reload()
        return False


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
