###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_photos.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: photos unit tests
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


class TestPhotos:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    # TOXINIDIR comes from tox.ini
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None) or os.environ.get('TOXINIDIR', None)

    store_mapping = {'generic': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__photos_page_2.json']),
                     'curated': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__photos_curated_page_2.json']),
                     'random': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__photos_random_count_2.json'])}

    @responses.activate
    def test_photos_generic(self):
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
        photos = pu_obj.photos(type_=type)
        assert photos.body is not None
        assert photos.header is not None
        assert photos.status_code == 200
        for photo in photos.entries:
            # if any of the fields breaks, then it's a problem
            print(photo.id, photo.link_html, photo.link_download, photo.link_download_location)   # , photo.stats  # TODO: include stats in unit test

    @responses.activate
    def test_photos_curated(self):
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
        photos = pu_obj.photos(type_=type)
        assert photos.body is not None
        assert photos.header is not None
        assert photos.status_code == 200
        for photo in photos.entries:
            # if any of the fields breaks, then it's a problem
            print(photo.id, photo.link_html, photo.link_download, photo.link_download_location)   # , photo.stats  # TODO: include stats in unit test

    @responses.activate
    def test_photos_random(self):
        type = 'random'
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
        photos = pu_obj.photos(type_=type)
        assert photos.body is not None
        assert photos.header is not None
        assert photos.status_code == 200
        for photo in photos.entries:
            # if any of the fields breaks, then it's a problem
            print(photo.id, photo.link_html, photo.link_download, photo.link_download_location)   # , photo.stats  # TODO: include stats in unit test
            print(photo.get_attribution())
            print(photo.get_attribution(format='str'))
            print(photo.get_attribution(format='html'))
