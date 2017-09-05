import pyunsplash
import logging
API_KEY='12e17a7db21afeff89fa5bfa990bc61205a2bc45cdc6672e4717abfaa3d5940c'


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




def main():
    pu, logger = funzione_1()
    funzione_2(pu, logger)
    funzione_3(pu, logger)
    

if __name__ == '__main__':
    main()
