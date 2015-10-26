#!/usr/bin/python
from os.path import join, abspath
from config.config import DUMP_PATH
import json


def dump_json(token_dict, filename):
    dump_path = abspath(join(DUMP_PATH, filename))
    with open(dump_path, 'w') as output_file:
        json.dump(token_dict, output_file, indent=4)
