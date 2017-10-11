#!/usr/bin/env python

from __future__ import print_function, unicode_literals, division, absolute_import

from babelpy.parser import parse
from babelpy.reader import read_txt_file
from babelpy.babelfy import BabelfyClient
from pprint import pprint
import sys
import traceback
try:
    from babelpy.config.config import API_KEY, LANG
except:
    LANG = 'EN'
    API_KEY = None

def main():
    global API_KEY

    # Parse the command-line arguments.
    args = parse()

    if not API_KEY:
        API_KEY = args.get('api_key')
        # Ensure input text is unicode.
        if (sys.version < '3' and isinstance(API_KEY, str)) or (sys.version > '3' and isinstance(API_KEY, bytes)):
            API_KEY = API_KEY.decode('utf-8')
        elif not API_KEY:
            print('BabelFy API key is required.', file=sys.stderr)
            sys.exit()

    # Get the input text from cmd-line or file.
    if args.get('text'):
        text = [args.get('text')]
    elif args.get('text_file'):
        filepath = args.get('text_file')
        try:
            text = read_txt_file(filepath)
        except Exception as e:
            print('failed to read text', file=sys.stderr)
            sys.exit()
    else:
        print('need text data to babelfy. see --help option for usage.', file=sys.stderr)
        sys.exit()

    # Split the text into sentences.
    text_list = list()
    for txt in text:
        sentence = txt.replace('\n', '').strip()
        if (sys.version < '3' and isinstance(sentence, str)) or (sys.version > '3' and isinstance(sentence, bytes)):
            sentence = sentence.decode('utf-8')
        text_list.append(sentence)

    try:
        if text[-1] == '.':
            text_list = text_list[:-1]
    except:
        pass

    # Instantiate BabelFy client.
    params = dict()
    params['lang'] = LANG
    babel_client = BabelfyClient(API_KEY, params)

    # Store parsed data.
    entities = list()
    all_entities = list()
    merged_entities = list()
    all_merged_entities = list()

    # Babelfy the the text, sentence by sentence.
    for sentence in text_list:
        # Babelfy sentence.
        try:
            babel_client.babelfy(sentence)
        except Exception as e:
            traceback.print_exc()

        # Get entity data.
        if args.get('entities'):
            entities.append(babel_client.entities)

        # Get entity and non-entity data.
        if args.get('all_entities'):
            all_entities.append(babel_client.all_entities)

        # Get merged entities only.
        if args.get('merged_entities'):
            merged_entities.append(babel_client.merged_entities)

        # Get all merged entities.
        if args.get('all_merged_entities'):
            all_merged_entities.append(babel_client.all_merged_entities)

    # Export to file.
    if args.get('export'):
        from dump import dump_json

        # Get the filename from cmd-line args.
        dumppath = args.get('export')

        # Ensure filename is unicode
        if (sys.version < '3' and isinstance(dumppath, str)) or (sys.version > '3' and isinstance(dumppath, bytes)):
            dumppath = dumppath.decode('utf-8')

        dumppath = dumppath + '.json' if not dumppath.endswith('.json') \
            else dumppath

        output_data = dict()

        if args.get('entities'):
            output_data['entities'] = entities

        if args.get('all_entities'):
            output_data['all_entities'] = all_entities

        if args.get('merged_entities'):
            output_data['merged_entities'] = merged_entities

        if args.get('all_merged_entities'):
            output_data['all_merged_entities'] = all_merged_entities

        try:
            dump_json(output_data, dumppath)
        except Exception as e:
            print('failed to write file',file=sys.stderr)
            traceback.print_exc()

    # Print to stdout.
    if args.get('print'):

        if args.get('entities'):
            print('\nENTITIES')
            for token in entities:
                pprint(token)

        if args.get('all_entities'):
            print('\nALL ENTITIES')
            for token in all_entities:
                pprint(token)

        if args.get('merged_entities'):
            print('\nMERGED ENTITIES')
            for token in merged_entities:
                pprint(token)

        if args.get('all_merged_entities'):
            print('\nALL MERGED ENTITIES')
            for token in all_merged_entities:
                pprint(token)

if __name__ == '__main__':
    main()
