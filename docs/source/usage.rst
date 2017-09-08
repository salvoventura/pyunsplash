#####
Usage
#####

Creating an instance
====================
::

    import pyunsplash
    pu = pyunsplash.PyUnsplash(api_key='<your Unsplash Application ID>')

API keys can be obtained from `Unsplash Developers <https://unsplash.com/developers>`_.

--------------------------------------------------------------------------------

Authorization workflow
======================
TODO


--------------------------------------------------------------------------------

Error handling
==============
TODO


--------------------------------------------------------------------------------

Library logging
===============
The PyUnsplash library internal logging subsystem is driven by the application.
The default logging level of the library is set to be **logging.ERROR**.
If you want to access the library logging subsystem, you can fine-tune the logger
with id **PyUnsplash.logger_name** as per the following example:

.. code-block:: python

    from pyunsplash import PyUnsplash

    # Initialize app logging
    logger = logging.getLogger()
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    # pyunsplash logger defaults to level logging.ERROR
    # If you need to change that, use getLogger/setLevel
    # on the module logger, like this:
    logging.getLogger(PyUnsplash.logger_name).setLevel(logging.DEBUG)

    pu = PyUnsplash(api_key='<your Unsplash Application ID>')
    # ... continue

