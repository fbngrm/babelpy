BabelFy API Client
======================

Python `BabelFy <http://babelfy.org>`_ entity tagger. Can be used as a library or command-line tool. Compatible with
both Python 2.7 as well as Python 3.

Installation
---------------

::

    pip install babelpy

or clone this github repository and run ``python setup.py install``, optionally prepend the commands with ``sudo`` for
global installation.

Usage
-------

Add your Babelfy API Key to the config file or provide it as an argument.


Use as command-line tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    babelpy [-h] [-t  | -tf ] [-e] [-ae] [-m] [-am] [-p] [-ex]

**Options**::

    -h,  --help                 show a help message and exit
    -key --api-key              BabelFy API key
    -t   --text                 text to be annotated by BabelFy API
    -tf  --text-file            path to the file containing the input text
    -e,  --entities             get entity data
    -ae  --all-entities         get entity and non-entity data
    -m   --merged-entities      get merged entities only
    -am  --all-merged-entities  get all merged entities
    -p   --print                dump all babelfy data to stdout
    -ex  --export               filename of the output file

**Example**::

    babelpy -tf ~/data/fashion.txt -am -ex ~/data/fashion.json

See ``babelpy -h`` for help.

Use as a library
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python


    from babelfy import BabelfyClient


    # Instantiate BabelFy client.
    params = dict()
    params['lang'] = LANG
    babel_client = BabelfyClient(API_KEY, params)

    # Babelfy sentence.
    babel_client.babelfy(TEXT_TO_BE_BABELFIED)

    # Get entity data.
    print(babel_client.entities)

    # Get entity and non-entity data.
    print(babel_client.all_entities)

    # Get merged entities only.
    print(babel_client.merged_entities)

    # Get all merged entities.
    babel_client.all_merged_entities

Run Tests with ``python tests/run_tests.py``

License
-----------

GNU - GPL 3.0
