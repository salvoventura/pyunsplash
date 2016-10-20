################
Instance methods
################
* Authorization
* Current User
* Users
* Photos
* Collections
* Search
* Stats

Authorization
=============
TODO


Current User
============
TODO


Users
=====
**users.get(username, w, h)**
    Retrieve public details on a given user.
    Supplying the optional *w* or *h* parameters will result in the custom photo URL being added to the profile_image object.


    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    w           number    optional
    h           number    optional
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get(username='<username>')

----

**users.get_portfolio(username)**
    Retrieve a single user's portfolio link.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_portfolio(username='<username>')
        portfolio_url = json_body.get('url')

----

**users.get_following(username)**
    API location of users this user is following.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_following(username='<username>')

----

**users.get_followers(username)**
    API location of this user's followers.

    ========    ======    =================
    Argument    Type      Optional/Required
    ========    ======    =================
    username    string    required
    ========    ======    =================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_followers(username='<username>')

----

**users.get_photos(username, page, per_page, order_by)**
    Get a list of photos uploaded by a user.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    username    string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    order_by    string    optional (default: latest)    latest, oldest, popular
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=1, per_page=5, order_by='popular')

----

**users.get_likes(username, page, per_page, order_by)**
    Get a list of photos liked by a user.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    username    string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    order_by    string    optional (default: latest)    latest, oldest, popular
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=1, per_page=5, order_by='popular')

----

**users.get_collections(username, page, per_page)**
    Get a list of collections created by the user.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    username    string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.users.get_collections(username='<username>', page=1, per_page=2)

----

**users.get_next()**
    If the last object retrieved supported pagination, this will retrieve the 'next' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=1, per_page=2)
        # next page from same query
        json_body = pu.users.get_next()

----

**users.get_previous()**
    If the last object retrieved supported pagination, this will retrieve the 'previous' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=3, per_page=2)
        # previous page from same query
        json_body = pu.users.get_previous()

----

**users.get_first()**
    If the last object retrieved supported pagination, this will retrieve the 'first' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=3, per_page=2)
        # first page from same query
        json_body = pu.users.get_first()

----

**users.get_last()**
    If the last object retrieved supported pagination, this will retrieve the 'last' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=3, per_page=2)
        # last page from same query
        json_body = pu.users.get_last()

----

**users.has_next**
    If the last object retrieved supported pagination, returns 'True' if there is a 'next' page.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=3, per_page=2)
        while pu.users.has_next:
            json_body = pu.users.get_next()

----

**users.has_previous**
    If the last object retrieved supported pagination, returns 'True' if there is a 'previous' page.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.users.get_photos(username='<username>', page=30, per_page=2)
        while pu.users.has_previous:
            json_body = pu.users.get_previous()

----

Photos
======
**photos.get(id, w, h, rect)**
    Retrieve a single photo.

    Supplying the optional w or h parameters will result in the custom photo URL being added to the urls object.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    id          string    required
    w           number    optional
    h           number    optional
    rect        dict      optional (cropped rect)       {'x': <int>, 'y': <int>, 'w': <int>, 'h': <int>}
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.photos.get(id_='<image_id>')

----

**photos.get_stats(id)**
    Retrieve a single photo's stats.

    Views are currently updated once daily.

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    id          string    required
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_stats(id_='<image_id>')

----

**photos.get_download(id)**
    Retrieve a single photo's download link.

    Preferably hit this endpoint if a photo is downloaded in your application for use
    (example: to be displayed on a blog article, to be shared on social media, to be remixed, etc.).

    This is different than the concept of a view, which is tracked automatically when you hotlinking an image

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    id          string    required
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_download(id_='<image_id>')
        img_url = json_body.get('url')

----

**photos.get_all(page, per_page, order_by)**
    Get a single page from the list of all photos.

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    order_by    string    optional (default: latest)    latest, oldest, popular
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=1, per_page=5, order_by='popular')

----

**photos.get_curated(page, per_page, order_by)**
    Get a single page from the list of the curated photos (front-page's photos).

    The photo objects returned here are abbreviated. For full details use GET /photos/:id

    ========    ======    ==========================    ==========================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ==========================
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    order_by    string    optional (default: latest)    latest, oldest, popular
    ========    ======    ==========================    ==========================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=1, per_page=5, order_by='popular')

----

**photos.get_random(args)**
    Retrieve a single random photo, given optional filters.

    If supplying multiple category ID's, the resulting photos will be those that match all of the given categories,
    not ones that match any category.

    You can't use the collections and query parameters in the same request

    When supplying a count parameter - and only then - the response will be an array of photos,
    even if the value of count is 1.


    ===========    ===============================================================================================
    Argument       Notes
    ===========    ===============================================================================================
    category       Category ID('s) to filter selection. If multiple, comma-separated. (deprecated)
    collections    Public collection ID('s) to filter selection. If multiple, comma-separated.
    featured       Limit selection to featured photos.
    username       Limit selection to a single user.
    query          Limit selection to photos matching a search term.
    w              Image width in pixels.
    h              Image width in pixels.
    orientation    Filter search results by photo orientation. Valid values are landscape, portrait, and squarish.
    count          The number of photos to return. (Default: 1; max: 30)
    ===========    ===============================================================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_random()

----

**photos.get_next()**
    If the last object retrieved supported pagination, this will retrieve the 'next' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=1, per_page=2)
        # next page from same query
        json_body = pu.photos.get_next()

----

**photos.get_previous()**
    If the last object retrieved supported pagination, this will retrieve the 'previous' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=3, per_page=2)
        # previous page from same query
        json_body = pu.photos.get_previous()

----

**photos.get_first()**
    If the last object retrieved supported pagination, this will retrieve the 'first' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=3, per_page=2)
        # first page from same query
        json_body = pu.photos.get_first()

----

**photos.get_last()**
    If the last object retrieved supported pagination, this will retrieve the 'last' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=3, per_page=2)
        # last page from same query
        json_body = pu.photos.get_last()

----

**photos.has_next**
    If the last object retrieved supported pagination, returns 'True' if there is a 'next' page.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=1, per_page=2)
        while pu.photos.has_next:
            json_body = pu.photos.get_next()

----

**photos.has_previous**
    If the last object retrieved supported pagination, returns 'True' if there is a 'previous' page.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.photos.get_all(page=30, per_page=2)
        while pu.photos.has_previous:
            json_body = pu.photos.get_previous()

----


Collections
===========
**collections.get(id)**
    Retrieve a single collection.

    To view a user's private collections, the **read_collections** scope is required.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    id          string    required
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get(id_='<collection_id>')

----

**collections.get_related(id)**
    Retrieve a list of collections related to this one.

    To view a user's private collections, the **read_collections** scope is required.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    id          string    required
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_related(id_='<collection_id>')

----

**collections.get_all(page, per_page)**
    Get a single page from the list of featured collections.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=2, per_page=20)

----

**collections.get_all_featured(page, per_page)**
    Get a single page from the list of featured collections.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all_featured(page=1, per_page=4)

----

**collections.get_all_curated(page, per_page)**
    Get a single page from the list of curated collections.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all_curated(page=1, per_page=4)

----

**collections.get_photos(id, page, per_page)**
    Retrieve a collection's photos.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    id          string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_photos(id_=<collection_id>, page=1, per_page=4)

----

**collections.get_curated_photos(id, page, per_page)**
    Retrieve a curated collection's photos.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    id          string    required
    page        number    optional (default: 1)
    per_page    number    optional (default: 10)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_curated_photos(id_=<collection_id>, page=1, per_page=4)

----

**collections.get_next()**
    If the last object retrieved supported pagination, this will retrieve the 'next' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=1, per_page=2)
        # next page from same query
        json_body = pu.collections.get_next()

----

**collections.get_previous()**
    If the last object retrieved supported pagination, this will retrieve the 'previous' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=3, per_page=2)
        # previous page from same query
        json_body = pu.collections.get_previous()

----

**collections.get_first()**
    If the last object retrieved supported pagination, this will retrieve the 'first' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=3, per_page=2)
        # first page from same query
        json_body = pu.collections.get_first()

----

**collections.get_last()**
    If the last object retrieved supported pagination, this will retrieve the 'last' page from the same.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=3, per_page=2)
        # last page from same query
        json_body = pu.collections.get_last()

----

**collections.has_next**
    If the last object retrieved supported pagination, returns 'True' if there is a 'next' page.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=3, per_page=2)
        while pu.collections.has_next:
            json_body = pu.collections.get_next()

----

**collections.has_previous**
    If the last object retrieved supported pagination, returns 'True' if there is a 'previous' page.

    Returns 'False' otherwise.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.get_(api_key='<your Unsplash API key>')
        json_body = pu.collections.get_all(page=30, per_page=2)
        while pu.collections.has_previous:
            json_body = pu.collections.get_previous()

----

Search
============
**search.photos(query, page)**
    Get a single page of photo results for a query.

    Search results limited to 20 photos per page. The photo objects returned here are abbreviated.
    For full details use GET /photos/:id.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    query       string    required                      search terms
    page        number    optional (default: 1)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.search.photos(query='dog', page=1)

----

**search.collections(query, page)**
    Get a single page of photo results for a query.

    Get a single page of collection results for a query.
    Search results limited to 20 collections per page.

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    query       string    required                      search terms
    page        number    optional (default: 1)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.search.collections(query='horse,white', page=1)

----

**search.users(query, page)**
    Get a single page of photo results for a query.

    Get a single page of collection results for a query.
    Search results limited to 20 users per page

    ========    ======    ==========================    ================================================
    Argument    Type      Optional/Required             Notes
    ========    ======    ==========================    ================================================
    query       string    required                      search terms
    page        number    optional (default: 1)
    ========    ======    ==========================    ================================================


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.search.users(query='maui', page=1)

----


Stats
=====
**stats.get_total()**
    Get a list of counts for all of Unsplash.


    **Example**
    ::

        import pyunsplash
        pu = pyunsplash.PyUnsplash(api_key='<your Unsplash API key>')
        json_body = pu.stats.get_stats()

----



END
