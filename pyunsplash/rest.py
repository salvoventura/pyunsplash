###############################################################################
#
#      File: rest.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 12 Oct 2016
#   Purpose: Handler for REST API interaction
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging

import requests

logger = logging.getLogger('pyunsplash')


class Rest(object):
    def __init__(self, api_key):
        self._api_key = api_key
        self._req_headers = {
            'Accept-Version': 'v1',
            'Authorization': 'Client-ID %s' % api_key,
        }
        self._status_code = None
        self._body = None
        self._headers = None
        self._navigation = None

    def _query_parameters(self, query_parameters):
        """
        Prepare the query parameter string to be appended to the url

        :param query_parameters: dictionary of query parameters and their values
        :return:
        """
        if query_parameters is None:
            return ''

        tmp = []
        for k, v in query_parameters.items():
            if v is None:
                continue
            if k == 'rect':
                tmp.append('{}={}'.format(k, ','.join(map(str, v.values()))))
            else:
                tmp.append('{}={}'.format(k, v))
        return '&'.join(tmp)

    def _parse_pagination(self, headers):
        _pag_dict = {'first': None, 'prev': None, 'next': None, 'last': None}
        pagination = headers.get('Link', None)
        if pagination:
            for item in pagination.split(','):
                # rel="first", rel="prev", rel="next", rel="last"
                link, rel = [l.strip(' <>') for l in item.split(';')]
                # here rel value is 'rel="next"'
                if rel[5:-1] in _pag_dict.keys():
                    _pag_dict[rel[5:-1]] = link
        return _pag_dict

    @property
    def status_code(self):
        return self._status_code

    @property
    def body(self):
        return self._body

    @property
    def headers(self):
        return self._headers

    @property
    def links(self):
        if hasattr(self.body, 'links'):
            return self.body.get('links')
        return {}

    @property
    def navigation(self):
        return self._navigation

    def get(self, url, query_params=None):
        _url = url
        if query_params:
            if url.find('?') > 0:
                _url = '&'.join([url, self._query_parameters(query_params)])
            else:
                _url = '?'.join([url, self._query_parameters(query_params)])

        _r = requests.get(_url, headers=self._req_headers, allow_redirects=True)

        try:
            self._status_code = _r.status_code
            self._headers = _r.headers
            self._body = _r.json()
            if self._status_code != requests.codes.ok:
                logger.error(
                    'HTTP status {}: {}'.format(self._status_code, self._body.get('errors', ['No error message'])))

        except ValueError, e:
            # If you get a 403, the body is NOT json...
            # thus need to protect this path
            logger.error('EXCEPTION: {}'.format(e))
            if self._status_code != requests.codes.ok:
                logger.error(
                    'HTTP status {}: {}'.format(self._status_code, _r.text))
            raise

        logger.debug('rest get {}'.format(_url))
        logger.debug('rest rsp status {} body {} headers {}'.format(self._status_code, self._body, self._headers))
        self._navigation = self._parse_pagination(self._headers)
        logger.debug('navigation {}'.format(self._navigation))
        return self._body

    def put(self, url, body):
        pass

    def post(self, url, body):
        pass

    def delete(self, url):
        pass


