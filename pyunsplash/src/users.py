###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: users.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose: Handles Users, and User
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .unpage import UnsplashPage
from .unobject import UnsplashObject
from .collections import Collections
from .photos import Photos


class Users(UnsplashPage):
    def __init__(self, api_key, url, **kwargs):
        valid_options = []
        super(Users, self).__init__(url=url, api_key=api_key, valid_options=valid_options, **kwargs)

    @property
    def entries(self):
        for entry in self.body:
            yield User(api_key=self.api_key, source=entry)


class User(UnsplashObject):
    def __init__(self, api_key, source, **kwargs):
        valid_options = ['w', 'h']
        # simplify for source=username
        if isinstance(source, str) and not source.startswith(self._api_root):
            # assume it's a userid
            source = "{}/users/{}".format(self._api_root, source)
        super(User, self).__init__(api_key=api_key, source=source, valid_options=valid_options, **kwargs)

    @property
    def link_html(self):
        return self.links.get('html', None)

    @property
    def link_portfolio(self):
        # no sense in retrieving the link, then the body etc...
        # unless this changes in the future
        return self.body.get('portfolio_url', None)

    @property
    def link_photos(self):
        return self.links.get('photos')

    @property
    def link_followers(self):
        return self.links.get('followers')

    @property
    def link_following(self):
        return self.links.get('following')

    def photos(self, **kwargs):
        # TODO: cache the returned object
        url = self.link_photos
        return Photos(url=url, api_key=self.api_key, **kwargs)

    def followers(self, **kwargs):
        # TODO: cache the returned object
        url = self.link_followers
        return Users(url=url, api_key=self.api_key, **kwargs)

    def following(self, **kwargs):
        # TODO: cache the returned object
        url = self.link_following
        return Users(url=url, api_key=self.api_key, **kwargs)

    def likes(self, **kwargs):
        # TODO: cache the returned object
        url = '{}/likes'.format(self.url)
        return Photos(url=url, api_key=self.api_key, **kwargs)

    def collections(self, **kwargs):
        # TODO: cache the returned object
        url = '{}/collections'.format(self.url)
        return Collections(url=url, api_key=self.api_key, **kwargs)

    def statistics(self, **kwargs):
        # TODO: cache the returned object
        # https://unsplash.com/documentation#get-a-users-statistics
        source = '{}/statistics'.format(self.url)
        return UserStatistics(api_key=self.api_key, source=source, **kwargs)


class UserStatistics(UnsplashObject):
    def __init__(self, api_key, source, **kwargs):
        valid_options = ['resolution', 'quantity']
        super(UserStatistics, self).__init__(api_key=api_key, source=source, valid_options=valid_options, **kwargs)

    @property
    def downloads(self):
        return self.body.get('downloads', None)

    @property
    def views(self):
        return self.body.get('views', None)

    @property
    def likes(self):
        return self.body.get('likes', None)
