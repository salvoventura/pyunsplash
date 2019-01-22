###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: collections.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 06 Dec 2016
#   Purpose: Handle Collections, CuratedCollections, FeaturedCollections, and Collection
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
from .liblogging import logger
from .unpage import UnsplashPage
from .unobject import UnsplashObject
from .photos import Photos


class Collections(UnsplashPage):
    def __init__(self, api_key, url='/collections', **kwargs):
        valid_options = ['page', 'per_page']
        super(Collections, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield Collection(api_key=self.api_key, source=entry)


class CuratedCollections(UnsplashPage):
    # TODO: 2019 this endpoint is deprecated
    def __init__(self, api_key, url='/collections/curated', **kwargs):
        logger.warning('This endpoint has been deprecated by the Unsplash API')
        valid_options = ['page', 'per_page']
        super(CuratedCollections, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield Collection(api_key=self.api_key, source=entry)


class FeaturedCollections(UnsplashPage):
    def __init__(self, api_key, url='/collections/featured', **kwargs):
        valid_options = ['page', 'per_page']
        super(FeaturedCollections, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield Collection(api_key=self.api_key, source=entry)


class Collection(UnsplashObject):
    def __init__(self, api_key, source):
        super(Collection, self).__init__(api_key=api_key, source=source)

    @property
    def title(self):
        return self.body.get('title', None)

    @property
    def description(self):
        return self.body.get('description', None)

    @property
    def user(self):
        return self.body.get('user', None)

    @property
    def link_photos(self):
        return self.links.get('photos')

    @property
    def link_related(self):
        return self.links.get('related')

    @property
    def related(self):
        # Apparently, 'related' doesn't honor parameters
        # TODO: cache the returned object
        url = self.link_related
        return Collections(url=url, api_key=self.api_key)

    def photos(self, **kwargs):
        # TODO: cache the returned object
        url = self.link_photos
        return Photos(url=url, api_key=self.api_key, **kwargs)
