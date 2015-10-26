#!/usr/bin/python


def read_txt_file(filepath):
    with open(filepath) as txt_file:
        return txt_file.read().replace('\n', '')
