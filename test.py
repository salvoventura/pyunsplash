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
        i+=1
    photo = p.get_next()
    photo_id = photo[0].get('id')
    print photo_id
    print p.get(id_=photo_id)
    print p.get_stats(id_=photo_id)
    print p.get_download(id_=photo_id)





if __name__ == '__main__':
    # users()
    photos()