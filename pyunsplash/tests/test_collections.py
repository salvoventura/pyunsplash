###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_collections.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: collections unit tests
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


class TestCollections:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None)
    print '>>>>', root_path, '<<<<'
    root_path = os.environ.get('WORKSPACE', None)
    print '>>>>', root_path, '<<<<'
    print os.environ

    store_mapping = {'generic': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__collections_page_2.json']),
                     'curated': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__collections_curated_page_2.json']),
                     'featured': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__collections_featured_page_2.json'])}

    @responses.activate
    def test_collections_generic(self):
        type = 'generic'
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
        collections = pu_obj.collections(type_=type)
        assert collections.body is not None
        assert collections.header is not None
        assert collections.status_code == 200
        for collection in collections.entries:
            # if any of the fields breaks, then it's a problem
            print(collection.id, collection.title, collection.description, collection.user, collection.link_photos, collection.link_related)
        assert collections.link_next is not None
        assert collections.link_previous is not None
        assert collections.link_first is not None
        assert collections.link_last is not None

    @responses.activate
    def test_collections_curated(self):
        type = 'curated'
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
        collections = pu_obj.collections(type_=type)
        assert collections.body is not None
        assert collections.header is not None
        assert collections.status_code == 200
        for collection in collections.entries:
            print(collection.id, collection.title, collection.description, collection.user, collection.link_photos, collection.link_related)
        assert collections.link_next is not None
        assert collections.link_previous is not None
        assert collections.link_first is not None
        assert collections.link_last is not None

    @responses.activate
    def test_collections_featured(self):
        type = 'featured'
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
        collections = pu_obj.collections(type_=type)
        assert collections.body is not None
        assert collections.header is not None
        assert collections.status_code == 200
        for collection in collections.entries:
            print(collection.id, collection.title, collection.description, collection.user, collection.link_photos, collection.link_related)
        assert collections.link_next is not None
        assert collections.link_previous is not None
        assert collections.link_first is not None
        assert collections.link_last is not None
