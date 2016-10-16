import logging
from logging.handlers import RotatingFileHandler

from .collections import Collections
from .photos import Photos
from .search import Search
from .stats import Stats
from .users import Users


def init_logging(log_level=logging.CRITICAL):
    log_filepath = 'pyunsplash.log'
    logging.basicConfig(level=log_level)
    logger = logging.getLogger("pyunsplash")
    handler = RotatingFileHandler(log_filepath, maxBytes=1024 * 1024 * 10, backupCount=10)
    handler.setLevel(log_level)
    formatter = logging.Formatter(
                    "%(asctime)s %(name)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
