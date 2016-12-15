###############################################################################
#
#      File: search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose:
#
#   Comment:
#
###############################################################################
import logging
from .unpage import UnsplashPage
from .collections import Collections
from .photos import Photos
from .users import Users
from .settings import LIB_NAME

logger = logging.getLogger(LIB_NAME)


class Search(UnsplashPage):
    def __init__(self, api_key, where, **kwargs):
        valid_options = ['page', 'per_page', 'query']
        url = None
        self.where = None
        if where.lower() in ['photos', 'collections', 'users']:
            self.where = where.lower()
            url = '/search/{}'.format(where.lower())
        super(Search, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        if self.where == 'photos':
            class_cast = Photos
        elif self.where == 'collections':
            class_cast = Collections
        elif self.where == 'users':
            class_cast = Users
        for entry in self.body.get('results', []):
            yield class_cast(api_key=self.api_key, source=entry)
