###############################################################################
#
#      File: test_search.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: search unit tests
#
#   Comment: use local resources
#
###############################################################################
import responses
import json
from pyunsplash import PyUnsplash
from pyunsplash.src.settings import API_ROOT

api_key = 'DUMMY_API_KEY'


class TestSearch:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    store_mapping = {
        'collections': 'resources/resource__search_collections_query_tree.json',
        'photos': 'resources/resource__search_photos_query_blue.json',
        'users': 'resources/resource__search_users_query_ventura.json',
    }

    @responses.activate
    def test_stats_total(self):
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
        for entry in search.entries:
            print entry.__class__
