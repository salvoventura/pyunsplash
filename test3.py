import logging

import pyunsplash

logger = logging.getLogger('pyunsplash')

pu = pyunsplash.PyUnsplash(api_key='ea8d39d41467c530ce8aa50b36cc1dd31d8527e6608656b729c270b9b8eaae79')
pu.init_logging(logging.DEBUG)
logger.debug("="*80)
logger.debug("New record")
logger.debug("="*80)

simple = pu.collections.get_all()
print simple
while pu.collections.has_next:
    simple = pu.collections.get_next()
    print '>>', simple




curated = pu.collections.get_curated()
print curated

featured = pu.collections.get_featured()
print featured

for collection in simple:
    print collection.get_related()
    for photo in collection.get_photos():
        print photo.get_stats()
    break

