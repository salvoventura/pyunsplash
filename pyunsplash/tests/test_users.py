###############################################################################
#
#      File: test_users.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: users unit tests
#
#   Comment: use local resources
#
###############################################################################
import responses
import json
from pyunsplash import PyUnsplash
from pyunsplash.src.settings import API_ROOT

api_key = 'DUMMY_API_KEY'


class TestUsers:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    store_mapping = {'salvoventura': 'resources/resource__users_salvoventura.json'}

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
        user = pu_obj.user(source=type)
        print(user.id, user.link_html, user.link_portfolio, user.link_following, user.link_followers, user.link_photos)

    # TODO: collections, photos and users from the user object
