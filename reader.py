#!/usr/bin/python


def read_txt_file(filepath):
    """read text from `filepath` and remove linebreaks
    """
    with open(filepath) as txt_file:
        return txt_file.read().replace('\n', '').strip()
