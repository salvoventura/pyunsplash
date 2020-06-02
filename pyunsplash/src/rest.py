###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: rest.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 12 Oct 2016
#   Purpose: Handler for REST API interaction
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
import requests
from .liblogging import logger


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

    @staticmethod
    def _query_parameters(query_parameters):
        """
        Prepare the query parameter string to be appended to the url

        :param query_parameters: dictionary of query parameters and their values
        :return:
        """
        logger.debug('calling _query_parameters(%s)', query_parameters)
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

    def get(self, url, query_params=None):
        logger.debug('calling rest get %s %s', url, query_params)
        _url = url
        if query_params:
            if url.find('?') > 0:
                _url = '&'.join([url, self._query_parameters(query_parameters=query_params)])
            else:
                _url = '?'.join([url, self._query_parameters(query_parameters=query_params)])

        logger.debug('rest get %s', _url)
        _r = requests.get(_url, headers=self._req_headers, allow_redirects=True)

        try:
            self._status_code = _r.status_code
            self._headers = _r.headers
            self._body = _r.json()
            if self._status_code != requests.codes.ok:
                logger.error(
                    'HTTP status %s: %s', self._status_code, self._body.get('errors', ['No error message'])
                )

        except ValueError as e:
            # If you get a 403, the body is NOT json
            # Good for logging, but can't really protect much, as anyway the
            # object up is likely going to run into its own exception for unexpected
            # result, and will make debugging this so much more difficult.
            # With some use, might get a better/smarter way of dealing with this.
            logger.error('EXCEPTION: %s', e)
            if self._status_code != requests.codes.ok:
                logger.error('HTTP EXC status %s: %s', self._status_code, _r.text)
            raise

        logger.debug('rest rsp status %s body %s headers %s', self._status_code, str(self._body).encode("utf-8"), self._headers)
        return _r

    def put(self, url, body):
        pass

    def post(self, url, body):
        pass

    def delete(self, url):
        pass
