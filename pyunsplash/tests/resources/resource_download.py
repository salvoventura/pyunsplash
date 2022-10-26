###############################################################################
#
#      File: resource_download.py
#
#    Author: Salvatore Ventura <salvoventura@gmail.com>
#      Date: 14 Dec 2016
#   Purpose: Download and save resources for unit testing
#
#   Comment: The APPLICATION ID is taken from OS ENV
#
###############################################################################
from pyunsplash.src.settings import API_ROOT
import requests
import os
import json
import time

api_key = os.environ['APPLICATION_ID']

req_headers = {
    'Accept-Version': 'v1',
    'Authorization': 'Client-ID %s' % api_key,
}


def _save_content(sub_url):
    url = '{}{}'.format(API_ROOT, sub_url)
    r = requests.get(url=url, headers=req_headers)

    out = {
        'url': sub_url,
        'body': r.json(),
        'headers': dict(r.headers),
        'status_code': r.status_code,
        'last_update': time.ctime()
    }

    # save to file
    filename = sub_url.replace('/', '_').replace('?', '_').replace('=', '_')
    print(os.getcwd())
    filepath = os.sep.join(['.', 'pyunsplash', 'tests', 'resources', 'resource_{}.json'.format(filename)])
    with open(filepath, 'w') as f:
        f.write(json.dumps(out))


def get_resources_collections():
    for sub_url in ['/collections?page=2', '/collections/featured?page=2']:
        _save_content(sub_url)


def get_resources_photos():
    for sub_url in ['/photos?page=2', '/photos/random?count=2']:
        _save_content(sub_url)


def get_resources_stats():
    for sub_url in ['/stats/total']:
        _save_content(sub_url)


def get_resources_users():
    for sub_url in ['/users/salvoventura', '/users/salvoventura/statistics']:
        _save_content(sub_url)


def get_resources_search():
    for sub_url in ['/search/photos?query=blue', '/search/collections?query=tree', '/search/users?query=ventura']:
        _save_content(sub_url)


def main():
    get_resources_collections()
    get_resources_photos()
    get_resources_stats()
    get_resources_users()
    get_resources_search()


if __name__ == '__main__':
    main()
