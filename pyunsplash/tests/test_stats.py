###############################################################################
#    Copyright (c) 2016 Salvatore Ventura <salvoventura@gmail.com>
#
#      File: test_stats.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: stats unit tests
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


class TestStats:
    # TODO: avoid code duplication
    # Need to workout how to combine responses.activate so as to avoid
    # code duplication, as the testcases are pretty much the same for all

    # On Jenkins, WORKDIR, comes from tox.ini
    root_path = os.environ.get('TRAVIS_BUILD_DIR', None) or os.environ.get('WORKDIR', None)

    store_mapping = {'total': os.sep.join([root_path, 'pyunsplash', 'tests', 'resources', 'resource__stats_total.json'])}

    @responses.activate
    def test_stats_total(self):
        type = 'total'
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
        stats = pu_obj.stats()
        # TODO: implement after successful stats download
        print(stats.total)
