from os.path import join, abspath
from config.config import DUMP_PATH
import sys
import json


def dump_json(token_dict, dump_path):
    """write json data to file
    """
    if sys.version > '3':
        with open(dump_path, 'w', encoding='utf-8') as output_file:
            json.dump(token_dict, output_file, indent=4)
    else:
        with open(dump_path, 'w') as output_file:
            json.dump(token_dict, output_file, indent=4)
