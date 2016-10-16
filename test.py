import logging

import pyunsplash

pyunsplash.init_logging(logging.DEBUG)
logger = logging.getLogger('pyunsplash')
logger.debug("="*80)
logger.debug("New record")
logger.debug("="*80)


def users():
    u = pyunsplash.Users()
    print u.get(username='salvoventura')
    # u.get_followers()
    # u.get_following()
    print u.get_likes(username='salvoventura')
    while u.has_next:
        print u.get_next()
    print u.get_portfolio(username='salvoventura')
    print u.get_photos(username='salvoventura', per_page=2, page=3)
    while u.has_next:
        print u.get_next()
    print u.get_following(username='salvoventura')
    print u.get_followers(username='salvoventura')


def photos():
    p = pyunsplash.Photos()
    print p.get_all(per_page=1)
    i=0
    while p.has_next and i<10:
        print i, p.get_next()
        i += 1
    photo = p.get_next()
    photo_id = photo[0].get('id')
    print photo_id
    print p.get(id_=photo_id)
    print p.get_stats(id_=photo_id)
    print p.get_download(id_=photo_id)


def search():
    s = pyunsplash.Search()
    print s.photos(query='dog,black', page=2)
    print s.collections(query='horse,white', page=1)
    print s.users(query='salvo',page=1)


def collections():
    c = pyunsplash.Collections()
    print c.get_all(per_page=1, page=2)
    print c.get_all_curated(page=3)
    print c.get_all_featured(per_page=3)
    collection = c.get_next()
    collection_id = collection[0].get('id')
    print collection_id
    print c.get(collection_id)
    print c.get_related(collection_id)
    print c.get_photos(collection_id, per_page=1, page=1)
    print c.get_curated_photos(collection_id)




def stats():
    s = pyunsplash.Stats()
    print s.get_total()


if __name__ == '__main__':
    # users()
    # photos()
    # search()
    collections()
    # stats()