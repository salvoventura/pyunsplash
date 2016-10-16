import pyunsplash

pu = pyunsplash.PyUnsplash(api_key='ea8d39d41467c530ce8aa50b36cc1dd31d8527e6608656b729c270b9b8eaae79')
# pu.init_logging(logging.DEBUG)

def test_users():
    print pu.users.get(username='salvoventura')
    print pu.users.get_likes(username='salvoventura')
    while pu.users.has_next:
        print pu.users.get_next()
    print pu.users.get_portfolio(username='salvoventura')
    print pu.users.get_photos(username='salvoventura', per_page=2, page=3)
    while pu.users.has_next:
        print pu.users.get_next()
    print pu.users.get_following(username='salvoventura')
    print pu.users.get_followers(username='salvoventura')


def test_photos():
    print pu.photos.get_all(per_page=1)
    i = 0
    while pu.photos.has_next and i < 10:
        print i, pu.photos.get_next()
        i += 1
    photo = pu.photos.get_next()
    photo_id = photo[0].get('id')
    print photo_id
    print pu.photos.get(id_=photo_id)
    print pu.photos.get_stats(id_=photo_id)
    print pu.photos.get_download(id_=photo_id)


def test_search():
    print pu.search.photos(query='dog,black', page=2)
    print pu.search.collections(query='horse,white', page=1)
    print pu.search.users(query='salvo', page=1)


def test_collections():
    print pu.collections.get_all(per_page=1, page=2)
    print pu.collections.get_all_curated(page=3)
    print pu.collections.get_all_featured(per_page=3)
    collection = pu.collections.get_next()
    collection_id = collection[0].get('id')
    print collection_id
    print pu.collections.get(collection_id)
    print pu.collections.get_related(collection_id)
    print pu.collections.get_photos(collection_id, per_page=1, page=1)
    print pu.collections.get_curated_photos(collection_id)


def test_stats():
    print pu.stats.get_total()


if __name__ == '__main__':
    test_users()
    test_photos()
    test_search()
    test_collections()
    test_stats()
