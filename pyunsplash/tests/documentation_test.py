import pyunsplash
import logging
API_KEY='ea8d39d41467c530ce8aa50b36cc1dd31d8527e6608656b729c270b9b8eaae79'


def funzione_1():
    pu = pyunsplash.PyUnsplash(api_key=API_KEY)
    pu.init_logging(logging.DEBUG)
    logger = logging.getLogger('pyunsplash')
    logger.info('Funzione_1')
    return pu, logger


def funzione_2(pu, logger):
    logger.info('Funzione_2')
    this_user = pu.user('salvoventura', w=100, h=100)


def funzione_3(pu, logger):
    logger.info('Funzione_3')
    # retrieve a page from the featured collections, with a maximum
    # of 5 collections per-page
    collections_page = pu.collections(type='featured', per_page=5)


def funzione_4(pu, logger):
    logger.info('Funzione_4')
    #
    #
    search = pu.search(type='photos', query='red,car')
    for entry in search.entries:
        print entry.link_html


def funzione_5(pu, logger):
    logger.info('Funzione_5')
    stats = pu.stats()
    print stats.total  # this is json


def funzione_6(pu, logger):
    logger.info('Funzione_6')
    pu.init_logging(logging.DEBUG)
    # use the PyUnsplash objects: all logs will be recorded to log file




# API: Class Collection

def funzione_7(pu, logger):
    logger.info('Funzione_7')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        collection.refresh()
        print collection.id


def funzione_8(pu, logger):
    logger.info('Funzione_8')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        print collection.id


def funzione_9(pu, logger):
    logger.info('Funzione_9')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        print collection.title


def funzione_10(pu, logger):
    logger.info('Funzione_10')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        print collection.description


def funzione_11(pu, logger):
    logger.info('Funzione_11')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        print collection.user


def funzione_12(pu, logger):
    logger.info('Funzione_12')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        print collection.link_photos


def funzione_13(pu, logger):
    logger.info('Funzione_13')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        print collection.link_related


def funzione_14(pu, logger):
    logger.info('Funzione_14')
    collections_page = pu.collections(type='featured', per_page=5)
    for collection in collections_page.entries:
        photos = collection.photos(order_by='popular', per_page=3)
        for photo in photos.entries:
            print photo.id, photo.link_download


def funzione_15(pu, logger):
    logger.info('Funzione_15')
    collections_page = pu.collections(type='featured', per_page=5)
    for cur_collection in collections_page.entries:
        related_collections = collection.related()
        for rel_collection in related_collections.entries:
            print rel_collection.title, rel_collection.description




# API: Class Collections

def funzione_16(pu, logger):
    logger.info('Funzione_16')
    this_user = pu.user('salvoventura', w=100, h=100)
    collections = this_user.collections(page=1, per_page=5)
    for collection in collections.entries:
        print collection.id, collection.title




# API: Class Photo

def funzione_17(pu, logger):
    logger.info('Funzione_17')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos()  # photos is an instance of class Photos
    for photo in photos.entries:
        photo.refresh()
        print photo.id, photo.link_download


def funzione_18(pu, logger):
    logger.info('Funzione_18')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos()    # photos is an instance of class Photos
    for photo in photos.entries:
        photo.refresh()
        print photo.id, photo.link_download


def funzione_19(pu, logger):
    logger.info('Funzione_19')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos()  # photos is an instance of class Photos
    for photo in photos.entries:
        print photo.id, photo.link_html


def funzione_20(pu, logger):
    logger.info('Funzione_20')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos()  # photos is an instance of class Photos
    for photo in photos.entries:
        print photo.id, photo.link_download


def funzione_21(pu, logger):
    logger.info('Funzione_21')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos()  # photos is an instance of class Photos
    for photo in photos.entries:
        print photo.stats




# API: Class Photos

def funzione_22(pu, logger):
    logger.info('Funzione_22')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos()  # photos is an instance of class Photos
    for photo in photos.entries:
        print photo.id, photo.link_download




# API: Class Search

def funzione_23(pu, logger):
    logger.info('Funzione_23')
    search = pu.search(type='photos', query='red,car')
    for photo in search.entries:
        print photo.id, photo.link_download




# API: Class Stats

def funzione_24(pu, logger):
    logger.info('Funzione_24')
    stats = pu.stats()
    print stats.total




# API: Class User

def funzione_25(pu, logger):
    logger.info('Funzione_25')
    this_user = pu.user('salvoventura', w=100, h=100)
    this_user.refresh()

def funzione_26(pu, logger):
    logger.info('Funzione_26')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.id

def funzione_27(pu, logger):
    logger.info('Funzione_27')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.links

def funzione_28(pu, logger):
    logger.info('Funzione_28')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.link_html

def funzione_29(pu, logger):
    logger.info('Funzione_29')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.link_portfolio

def funzione_30(pu, logger):
    logger.info('Funzione_30')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.link_followers

def funzione_31(pu, logger):
    logger.info('Funzione_31')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.link_following

def funzione_32(pu, logger):
    logger.info('Funzione_32')
    this_user = pu.user('salvoventura', w=100, h=100)
    print this_user.link_photos

def funzione_33(pu, logger):
    logger.info('Funzione_33')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.photos(per_page=5)
    for photo in photos.entries:
        print photo.id, photo.link_download

def funzione_34(pu, logger):
    logger.info('Funzione_34')
    this_user = pu.user('salvoventura', w=100, h=100)
    followers = this_user.followers()
    for user in followers.entries:
        print user.id, user.body.get('first_name'), user.body.get('last_name')

def funzione_35(pu, logger):
    logger.info('Funzione_35')
    this_user = pu.user('salvoventura', w=100, h=100)
    following = this_user.following()
    for user in following.entries:
        print user.id, user.body.get('first_name'), user.body.get('last_name')

def funzione_36(pu, logger):
    logger.info('Funzione_36')
    this_user = pu.user('salvoventura', w=100, h=100)
    photos = this_user.likes(per_page=5)
    for photo in photos.entries:
        print photo.id, photo.link_download

def funzione_37(pu, logger):
    logger.info('Funzione_37')
    this_user = pu.user('salvoventura', w=100, h=100)
    collections = this_user.collections(page=1, per_page=5)
    for collection in collections.entries:
        print collection.id, collection.title




# API: Class Users

def funzione_38(pu, logger):
    logger.info('Funzione_38')
    this_user = pu.user('salvoventura', w=100, h=100)
    followers = this_user.followers()  # followers is an instance of class Users
    for user in followers.entries:
        print user.id, user.body.get('first_name'), user.body.get('last_name')


























def main():
    pu, logger = funzione_1()
    funzione_2(pu, logger)
    funzione_3(pu, logger)
    funzione_4(pu, logger)
    funzione_5(pu, logger)
    funzione_6(pu, logger)
    funzione_7(pu, logger)
    funzione_8(pu, logger)
    funzione_9(pu, logger)
    funzione_10(pu, logger)
    funzione_11(pu, logger)
    funzione_12(pu, logger)
    funzione_13(pu, logger)
    funzione_14(pu, logger)
    funzione_15(pu, logger)
    funzione_16(pu, logger)
    funzione_17(pu, logger)
    funzione_18(pu, logger)
    funzione_19(pu, logger)
    funzione_20(pu, logger)
    funzione_21(pu, logger)
    funzione_22(pu, logger)
    funzione_23(pu, logger)
    funzione_24(pu, logger)
    funzione_25(pu, logger)
    funzione_26(pu, logger)
    funzione_27(pu, logger)
    funzione_28(pu, logger)
    funzione_29(pu, logger)
    funzione_30(pu, logger)
    funzione_31(pu, logger)
    funzione_32(pu, logger)
    funzione_33(pu, logger)
    funzione_34(pu, logger)
    funzione_35(pu, logger)
    funzione_36(pu, logger)
    funzione_37(pu, logger)




if __name__ == '__main__':
    main()
