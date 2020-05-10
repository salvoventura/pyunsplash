###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: unpage.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 06 Dec 2016
#   Purpose: Base class for Unsplash API pages
#
#  Revision: 1
#   Comment: What's new in revision 1
#            Any object exposes GET/PUT/POST/DELETE
#               url is optional; if none provided, the current url is used
#               next, previous, last, first *might* be available and usable
#               object itself has no memory
#               GET, next, previous, last, first return a new object
#               POST returns TBD
#               PUT no returns (true/false or error...)
#               DELETE no returns (true, false or error...)
###############################################################################
from .liblogging import logger
from .rest import Rest
from .settings import API_ROOT


class UnsplashPage(object):
    _api_root = API_ROOT

    def __init__(self, url, api_key=None, valid_options=None, **kwargs):
        self.api_key = api_key
        self.valid_options = valid_options

        if url is None:
            raise ValueError('UnsplashPage: url cannot be None')

        self.url = self._sanitized_url(url)
        self.query_parameters = self._sanitized_query_parameters(kwargs)

        self._agent = None                            # potentially move outside init
        self.navigation = None
        self.requests = None

        if api_key is not None:
            self._agent = Rest(api_key=self.api_key)

        if self.url is not None:
            r = self._agent.get(self.url, self.query_parameters)
            if r.status_code == 200:
                self.requests = r
                self._parse_navigation()

    @property
    def body(self):
        if self.requests:
            return self.requests.json()

    @property
    def entries(self):
        # must override in child class
        raise NotImplementedError

    @property
    def header(self):
        if self.requests:
            return self.requests.headers

    @property
    def status_code(self):
        if self.requests:
            return self.requests.status_code

    def set_api_key(self, api_key):
        self.api_key = api_key
        self._agent = Rest(api_key=self.api_key)

    def get(self, url, query_parameters=None):
        return self.__class__(url=url, query_parameters=query_parameters, api_key=self.api_key)

    def put(self, url, body):
        # TODO
        pass

    def post(self, url, body):
        # TODO
        pass

    def delete(self, url):
        # TODO
        pass

    @property
    def link_self(self):
        return self._ret_link('self')

    @property
    def link_next(self):
        return self._ret_link('next')

    @property
    def link_previous(self):
        return self._ret_link('prev')

    @property
    def link_first(self):
        return self._ret_link('first')

    @property
    def link_last(self):
        return self._ret_link('last')

    @property
    def has_next(self):
        return self.link_next is not None

    @property
    def has_previous(self):
        return self.link_previous is not None

    def get_next_page(self):
        return self.__class__(url=self.link_next, api_key=self.api_key)

    def get_previous_page(self):
        return self.__class__(url=self.link_previous, api_key=self.api_key)

    def get_first_page(self):
        return self.__class__(url=self.link_first, api_key=self.api_key)

    def get_last_page(self):
        return self.__class__(url=self.link_last, api_key=self.api_key)

    def _sanitized_url(self, url):
        logger.debug('call _sanitized_url(%s)', url)
        if url.startswith(self._api_root):
            good_url = url
        elif url.startswith('/'):
            good_url = '{}{}'.format(self._api_root, url)
        else:
            good_url = '{}/{}'.format(self._api_root, url)
        logger.debug('     returning %s', good_url)
        return good_url

    def _sanitized_query_parameters(self, kwargs):
        logger.debug('call _sanitized_query_parameters(%s)', kwargs)
        query_params = {}
        for key in kwargs:
            # Raising an exception here: if we are too protective it will hurt debuggability
            if self.valid_options and key not in self.valid_options:
                logger.debug('Invalid parameter %s' % key)
                raise ValueError('Invalid parameter %s' % key)
            query_params[key] = kwargs[key]
        logger.debug('     returning %s', query_params)
        return query_params

    def _parse_navigation(self):
        navigation = {'self': self.url, 'first': None, 'prev': None, 'next': None, 'last': None}
        pagination = self.requests.headers.get('Link', None)
        if pagination:
            for item in pagination.split(','):
                # rel="first", rel="prev", rel="next", rel="last"
                link, rel = [l.strip(' <>') for l in item.split(';')]
                # here rel value is 'rel="next"'
                if rel[5:-1] in navigation.keys():
                    navigation[rel[5:-1]] = link
        self.navigation = navigation

    def _ret_link(self, which):
        if self.navigation:
            return self.navigation.get(which, None)
