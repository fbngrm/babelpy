#! /usr/bin/env python
# -*- coding: utf8 -*-

from __future__ import print_function

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "BabelPy",
    version = "1.0",
    author = "Marius Rehmet",
    author_email = "mr@vojd.net",
    description = ("BabelFy API Client"),
    license = "GPL",
    keywords = "nlp computational_linguistics entities wikipedia dbpedia linguistics",
    url = "https://github.com/fbngrm/babelpy",
    packages=['babelpy', 'babelpy.config', 'babelpy.tests'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    zip_safe=False,
    include_package_data=True,
    package_data = {'babelpy': ['tests/txt'] },
    install_requires=[],
    entry_points = {    'console_scripts': [ 'babelpy = babelpy.babelpy:main' ] }
)
