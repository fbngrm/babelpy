import sys

def read_txt_file(filepath):
    """read text from `filepath` and remove linebreaks
    """
    if sys.version > '3':
        with open(filepath,'r',encoding='utf-8') as txt_file:
            return txt_file.readlines()
    else:
        with open(filepath) as txt_file:
            return txt_file.readlines()
