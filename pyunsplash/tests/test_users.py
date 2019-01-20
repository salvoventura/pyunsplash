###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_users.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: users unit tests
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


class TestUsers:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    # TOXINIDIR comes from tox.ini
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None) or os.environ.get('TOXINIDIR', None)

    store_mapping = {
        'salvoventura':
            os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__users_salvoventura.json']),
        'salvoventura_statistics':
            os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__users_salvoventura_statistics.json'])
    }

    @responses.activate
    def test_stats_total(self):
        type = 'salvoventura'
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
        this_user = pu_obj.user(source=type)
        print(this_user.id, this_user.link_html, this_user.link_portfolio, this_user.link_following, this_user.link_followers, this_user.link_photos)

    # TODO: collections, photos and users from the user object

    @responses.activate
    def test_user_stats(self):
        username = 'salvoventura'

        # Add the user api response
        type = 'salvoventura'
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

        # Add the user statistics api response
        type = 'salvoventura_statistics'
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
        this_user = pu_obj.user(source=username)  # create a User object
        this_user_stats = this_user.statistics()  # fetch a UserStatistics object
        print(this_user_stats.downloads.get('total'), this_user_stats.views.get('total'), this_user_stats.likes.get('total'))
