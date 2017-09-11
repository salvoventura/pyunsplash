###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: search unit tests
#
#  Revision: 1
#   Comment: What's new in revision 1
#            use local resources
#
###############################################################################
import responses
import json
import os
from pyunsplash import PyUnsplash
from pyunsplash.src.settings import API_ROOT

api_key = os.environ.get('APPLICATION_ID', None) or 'DUMMY_APPLICATION_ID'


class TestSearch:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None) or os.environ.get('PYTHONPATH', None)

    store_mapping = {
        'collections': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__search_collections_query_tree.json']),
        'photos': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__search_photos_query_blue.json']),
        'users': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__search_users_query_ventura.json'])}

    @responses.activate
    def test_search_collections(self):
        type = 'collections'
        resource_filepath = self.store_mapping[type]
        stored_response = json.loads(open(resource_filepath).read())
        responses.add(
            responses.GET,
            '{}{}'.format(API_ROOT, stored_response.get('url').split('?')[0]),   # cheating on the url, because the class always inits without query params
            json=stored_response.get('body'),
            status=stored_response.get('status_code'),
            content_type='application/json',
            adding_headers=stored_response.get('headers')
        )
        pu_obj = PyUnsplash(api_key=api_key)
        search = pu_obj.search(type, query='tree')
        for collection in search.entries:
            print(collection.id, collection.title, collection.description, collection.user, collection.link_photos, collection.link_related)

    @responses.activate
    def test_search_photos(self):
        type = 'photos'
        resource_filepath = self.store_mapping[type]
        stored_response = json.loads(open(resource_filepath).read())
        responses.add(
            responses.GET,
            '{}{}'.format(API_ROOT, stored_response.get('url').split('?')[0]),   # cheating on the url, because the class always inits without query params
            json=stored_response.get('body'),
            status=stored_response.get('status_code'),
            content_type='application/json',
            adding_headers=stored_response.get('headers')
        )
        pu_obj = PyUnsplash(api_key=api_key)
        search = pu_obj.search(type, query='tree')
        for photo in search.entries:
            print(photo.id, photo.link_html, photo.link_download)  # , photo.stats  # TODO: include stats in unit test

    @responses.activate
    def test_search_users(self):
        type = 'users'
        resource_filepath = self.store_mapping[type]
        stored_response = json.loads(open(resource_filepath).read())
        responses.add(
            responses.GET,
            '{}{}'.format(API_ROOT, stored_response.get('url').split('?')[0]),   # cheating on the url, because the class always inits without query params
            json=stored_response.get('body'),
            status=stored_response.get('status_code'),
            content_type='application/json',
            adding_headers=stored_response.get('headers')
        )
        pu_obj = PyUnsplash(api_key=api_key)
        search = pu_obj.search(type, query='tree')
        for user in search.entries:
            print(user.id, user.link_html, user.link_portfolio, user.link_following, user.link_followers, user.link_photos)

