from os.path import join, abspath
from config.config import DUMP_PATH
import json


def dump_json(token_dict, dump_path):
    """write json data to file
    """
    with open(dump_path, 'w') as output_file:
        json.dump(token_dict, output_file, indent=4)
