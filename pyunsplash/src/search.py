###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 08 Dec 2016
#   Purpose: Handle Search
#
#  Revision: 1
#   Comment: What's new in revision 1
#
###############################################################################
# from .liblogging import logger
from .unpage import UnsplashPage
from .collections import Collection
from .photos import Photo
from .users import User


class Search(UnsplashPage):
    def __init__(self, api_key, url, **kwargs):
        valid_options = {
                "photos": [
                    "query",
                    "page",
                    "per_page",
                    "order_by",
                    "collections",
                    "content_filter",
                    "color",
                    "orientation",
                    "lang", # Beta parameter (for access to beta parameters, email api@unsplash.com with your application ID)
                ],
                "collections": [
                    "query",
                    "page",
                    "per_page",
                ],
                "users": [
                    "query",
                    "page",
                    "per_page",
                ],
        }
        self.url = url.lower()
        if self.url in valid_options:
            url = "/search/{}".format(url)
        super(Search, self).__init__(
            url=url, api_key=api_key, valid_options=valid_options[self.url], **kwargs
        )

    @property
    def entries(self):
        if self.url == "photos" or self.url.endswith("/photos"):
            class_cast = Photo
        elif self.url == "collections" or self.url.endswith("/collections"):
            class_cast = Collection
        elif self.url == "users" or self.url.endswith("/users"):
            class_cast = User
        for entry in self.body.get("results", []):
            yield class_cast(api_key=self.api_key, source=entry)
