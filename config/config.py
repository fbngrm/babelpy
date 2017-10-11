from os.path import abspath, join, dirname

ROOT_PATH = abspath(join(dirname(__file__), '..'))
DUMP_DIR = 'data'
DUMP_PATH = abspath(join(ROOT_PATH, DUMP_DIR))
BABELFY_API_URL = 'https://babelfy.io/v1/disambiguate'
LANG = 'EN'
API_KEY = None
BABELFY_API_URL = 'https://babelfy.io/v1/disambiguate'
