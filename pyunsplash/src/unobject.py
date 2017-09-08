###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: unobject.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 07 Dec 2016
#   Purpose: Base class for Unsplash API objects
#
#  Revision: 1
#   Comment: What's new in revision 1
#            The idea here is that, and object can be created in two ways:
#            - by its json body
#                 the body might be partial, but still the object provides
#                 shortcut/unified methods to deal with common data extraction
#                 A reload/refresh command can be issued to fetch data from the
#                 server, and the body gets updated
#            - by its url
#                 in this case an explicit API call is made to populate body
###############################################################################
from .liblogging import logger
from .rest import Rest
from .settings import API_ROOT


class UnsplashObject(object):
    _api_root = API_ROOT

    def __init__(self, api_key, source, valid_options=None, **kwargs):
        self.api_key = api_key
        self.valid_options = valid_options
        self.body, self.url, self._agent = None, None, None

        self.query_parameters = self._sanitized_query_parameters(kwargs)
        self._parse_source(source)  # sets self.body, self.url

        if not self._agent:
            self._agent = Rest(api_key=self.api_key)

    def refresh(self):
        if not self._agent:
            logger.debug('need an agent first')
            self._agent = Rest(api_key=self.api_key)

        logger.debug('object refresh from url %s', self.url)
        r = self._agent.get(self.url, self.query_parameters)
        if r.status_code == 200:
            logger.debug('status %s: loading object body', r.status_code)
            self.body = r.json()
        else:
            logger.debug('status %s: object body not refreshed', r.status_code)

    @property
    def id(self):
        return self.body.get('id', None)

    @property
    def links(self):
        return self.body.get('links', None)

    def _parse_source(self, source):
        # guess format based on source type, extract the link to self
        if isinstance(source, dict):
            logger.debug('Source is a dictionary')
            self.body = source
            self.url = source.get('links').get('self')
        #                                               # TODO: maybe protect and raise appropriate exception in
        elif isinstance(source, str):                   # case someone feeds a random dictionary here
            logger.debug('Source is a string')
            if source.startswith(self._api_root):
                self.url = source
                self.refresh()
            else:
                logger.info('Source is a string, but we did not handle it: %s', source)
                raise ValueError('Source is a string, but we did not handle it: %s' % source)
        else:
            logger.info('Invalid parameter to constructor: %s', source)
            raise ValueError('Invalid parameter to constructor: %s' % source)

    def _sanitized_query_parameters(self, kwargs):
        logger.debug('call _sanitized_query_parameters(%s)', kwargs)
        query_params = {}
        for key in kwargs:
            if self.valid_options and key not in self.valid_options:
                logger.info('invalid parameter %s, safely ignoring it', key)
                continue
            query_params[key] = kwargs[key]
        logger.debug('     returning %s', query_params)
        return query_params
