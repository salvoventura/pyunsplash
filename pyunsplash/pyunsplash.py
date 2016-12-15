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
import logging
from logging.handlers import RotatingFileHandler
from .src.settings import LIB_NAME
from .src.users import User
from .src.collections import Collections, FeaturedCollections, CuratedCollections
from .src.photos import Photos, CuratedPhotos, RandomPhotos
from .src.search import Search
from .src.stats import Stats

logger = logging.getLogger(LIB_NAME)


class PyUnsplash(object):
    def __init__(self, api_key):
        self._api_key = api_key

    # TODO: oAuth

    def user(self, source, **kwargs):
        return User(api_key=self._api_key, source=source, **kwargs)

    def collections(self, type='generic', **kwargs):
        lookup = {'curated': CuratedCollections,
                  'generic': Collections,
                  'featured': FeaturedCollections}

        if type in lookup:
            f = lookup.get(type)
            return f(api_key=self._api_key, **kwargs)

        logger.debug('No collections object to return')
        return None

    def photos(self, type='generic', **kwargs):
        lookup = {'curated': CuratedPhotos,
                  'generic': Photos,
                  'random': RandomPhotos}

        if type in lookup:
            f = lookup.get(type)
            return f(api_key=self._api_key, **kwargs)

        logger.debug('No photos object to return')
        return None

    def search(self, type, **kwargs):
        return Search(api_key=self._api_key, where=type, **kwargs)

    def stats(self):
        return Stats(api_key=self._api_key)

    @staticmethod
    def init_logging(log_level=logging.CRITICAL):
        """
        Initialize logging if required. Only needed for debugging.

        :param log_level: valid values from logging module
        :return: None
        """
        logging.basicConfig(level=log_level)
        logger = logging.getLogger(LIB_NAME)

        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        log_filepath = '{}.log'.format(LIB_NAME)

        handler = RotatingFileHandler(log_filepath, maxBytes=1024 * 1024 * 10, backupCount=10)
        handler.setLevel(log_level)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
