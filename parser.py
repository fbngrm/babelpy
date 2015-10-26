#!/usr/bin/python
import argparse


def parse():
        parser = argparse.ArgumentParser(
            description='BabelFy Entity Tagger',
            formatter_class=argparse.RawTextHelpFormatter
            )
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            '-t',
            '--text',
            help='text to be annotated by BabelFy API',
            metavar='',
            )
        group.add_argument(
            '-tf',
            '--text-file',
            help='path to the file containing the text to be annotated by \
                BabelFy API',
            metavar='',
            )
        parser.add_argument(
            '-e',
            '--entities',
            help='get entity data',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-ae',
            '--all-entities',
            help='get entity and non-entity data',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-m',
            '--merged-entities',
            help='get merged entities only',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-am',
            '--all-merged-entities',
            help='get all merged entities',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-p',
            '--print',
            help='dump all babelfy data to stdout',
            required=False,
            action='store_true',
            )
        parser.add_argument(
            '-ex',
            '--export',
            help='filename of the output file',
            required=False,
            metavar='',
            )

        return vars(parser.parse_args())
