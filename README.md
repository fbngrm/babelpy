# BabelFy API Client

Python [BabelFy](http://babelfy.org) entity tagger. Can be used as a library or command-line tool.

## Requirements
* Python 2.7
* wheel==0.24.0

## Usage
### Use as command-line tool

```python babelpy.py [-h] [-t  | -tf ] [-e] [-ae] [-m] [-am] [-p] [-ex]```


**Options**
```
-h,  --help                 *show a help message and exit*
-key --api-key              *BabelFy API key*
-t   --text                 *text to be annotated by BabelFy API*
-tf  --text-file            *path to the file containing the input text*
-e,  --entities             *get entity data*
-ae  --all-entities         *get entity and non-entity data*
-m   --merged-entities      *get merged entities only*
-am  --all-merged-entities  *get all merged entities*
-p   --print                *dump all babelfy data to stdout*
-ex  --export               *filename of the output file*
```

**Example**

```python babelpy.py -tf ~/data/fashion.txt -am -ex ~/data/fashion.json```

See python babelpy.py -h for help.

**Use as a library**
```
from babelfy import BabelfyClient


# Instantiate BabelFy client.
params = dict()
params['lang'] = LANG
babel_client = BabelfyClient(API_KEY, params)

# Babelfy sentence.
babel_client.babelfy(TEXT_TO_BE_BABELFIED)

# Get entity data.
print babel_client.entities

# Get entity and non-entity data.
print babel_client.all_entities

# Get merged entities only.
print babel_client.merged_entities

# Get all merged entities.
babel_client.all_merged_entities
```
