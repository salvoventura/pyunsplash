###############################################################################
#
#      File: pyunsplash.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose: Main class
#
#   Comment:
#
###############################################################################
from .src.liblogging import logger
from .src.collections import Collections, FeaturedCollections, CuratedCollections
from .src.photos import Photos, CuratedPhotos, RandomPhotos, SinglePhoto
from .src.search import Search
from .src.stats import Stats
from .src.users import User
from .src.settings import LIB_NAME


class PyUnsplash(object):
    logger_name = LIB_NAME

    def __init__(self, api_key):
        self._api_key = api_key

    # TODO: oAuth

    def user(self, source, **kwargs):
        return User(api_key=self._api_key, source=source, **kwargs)

    def collections(self, type_='generic', **kwargs):
        lookup = {'curated': CuratedCollections,  # 2019: DEPRECATED
                  'generic': Collections,
                  'featured': FeaturedCollections}

        if type_ in lookup:
            f = lookup.get(type_)
            return f(api_key=self._api_key, **kwargs)

        logger.debug('No collections object to return')
        return None

    def photos(self, type_='generic', **kwargs):
        lookup = {'curated': CuratedPhotos,  # 2019: DEPRECATED
                  'generic': Photos,
                  'random': RandomPhotos,
                  'single': SinglePhoto}

        if type_ in lookup:
            f = lookup.get(type_)
            return f(api_key=self._api_key, **kwargs)

        logger.debug('No photos object to return')
        return None

    def search(self, type_, **kwargs):
        return Search(api_key=self._api_key, url=type_, **kwargs)

    def stats(self):
        return Stats(api_key=self._api_key)
