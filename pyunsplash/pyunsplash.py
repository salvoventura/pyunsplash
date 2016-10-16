###############################################################################
#
#      File: pyunsplash.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 15 Oct 2016
#   Purpose: Main class
#
#  Revision: 1
#   Comment: First revision
#
###############################################################################
import logging
from logging.handlers import RotatingFileHandler

from .lib.collections import Collections
from .lib.photos import Photos
from .lib.search import Search
from .lib.stats import Stats
from .lib.users import Users

logger = logging.getLogger('pyunsplash')


class PyUnsplash():
    def __init__(self, api_key):
        self._api_key = api_key
        self.users = Users(api_key)
        self.photos = Photos(api_key)
        self.search = Search(api_key)
        self.collections = Collections(api_key)
        self.stats = Stats(api_key)

    # TODO: oAuth

    def init_logging(self, log_level=logging.CRITICAL):
        """
        Initialize logging if required. Only needed for debugging.

        :param log_level: valid values from logging module
        :return: None
        """
        log_filepath = 'pyunsplash.log'
        logging.basicConfig(level=log_level)
        logger = logging.getLogger("pyunsplash")
        handler = RotatingFileHandler(log_filepath, maxBytes=1024 * 1024 * 10, backupCount=10)
        handler.setLevel(log_level)
        formatter = logging.Formatter(
                        "%(asctime)s %(name)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
