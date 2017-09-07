###############################################################################
#
#      File: photos.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 07 Dec 2016
#   Purpose:
#
#   Comment:
#
###############################################################################
import logging
from .unpage import UnsplashPage
from .unobject import UnsplashObject
from .settings import LIB_NAME

logger = logging.getLogger(__name__)


class Photos(UnsplashPage):
    def __init__(self, api_key, url='/photos', **kwargs):
        valid_options = ['page', 'per_page', 'order_by']
        super(Photos, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield Photo(api_key=self.api_key, source=entry)


class CuratedPhotos(UnsplashPage):
    def __init__(self, api_key, url='/photos/curated', **kwargs):
        valid_options = ['page', 'per_page', 'order_by']
        super(CuratedPhotos, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield Photo(api_key=self.api_key, source=entry)


class RandomPhotos(UnsplashPage):
    def __init__(self, api_key, url='/photos/random', **kwargs):
        valid_options = ['category', 'collections', 'featured', 'username', 'query', 'w', 'h', 'orientation', 'count']
        super(RandomPhotos, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield Photo(api_key=self.api_key, source=entry)


class Photo(UnsplashObject):
    def __init__(self, api_key, source, **kwargs):
        valid_options = ['w', 'h', 'rect']
        # simplify for source=photoid
        if isinstance(source, str) and not source.startswith(self._api_root):
            # assume it's a photoid
            source = "{}/photos/{}".format(self._api_root, source)
        super(Photo, self).__init__(api_key=api_key, source=source, valid_options=valid_options, **kwargs)

    @property
    def link_html(self):
        return self.links.get('html', None)

    @property
    def stats(self):
        url = '{}/stats'.format(self.url)
        r = self._agent.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            logger.debug('Failed stats retrieval for {} with status code {}'.format(url, r.status_code))
            return None

    def link_download(self, **kwargs):
        return self.links.get('download')

