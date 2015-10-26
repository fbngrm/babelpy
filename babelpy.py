#!/usr/bin/python

from parser import parse
from reader import read_txt_file
from babelfy import BabelfyClient
from config.config import API_KEY, LANG
from pprint import pprint
import sys


# Parse the command-line arguments.
args = parse()

# Get the input text from cmd-line or file.
if args.get('text'):
    text = args.get('text')
elif args.get('text_file'):
    filepath = args.get('text_file')
    text = read_txt_file(filepath)
else:
    print 'Need text data to Babelfy. See --help option for usage.'
    sys.exit()

# Ensure input text is an instance of unicode.
if isinstance(text, str):
    text = text.decode('utf-8')

# Remove mltiple whitspaces from the text.
text = ' '.join(x.strip() for x in text.split())

# Split the text into sentences.
text_list = [x.strip() + '.' for x in text.split('.')] or [text]
if text[-1] == '.':
    text_list = text_list[:-1]

# Instantiate BabelFy client.
params = dict()
params['lang'] = LANG,
babel_client = BabelfyClient(API_KEY, params)

# Store parsed data.
entities = list()
all_entities = list()
merged_entities = list()
all_merged_entities = list()

# Babelfy the the text, sentence by sentence.
for sentence in text_list:
    # Babelfy sentence.
    babel_client.babelfy(sentence)

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
    filename = args.get('export')

    # Ensure filename is an instance of unicode.
    if isinstance(filename, str):
        filename = filename.decode('utf-8')

    filename = filename + '.json' if not filename.endswith('.json') \
        else filename

    output_data = dict()

    if args.get('entities'):
        output_data['entities'] = entities

    if args.get('all_entities'):
        output_data['all_entities'] = all_entities

    if args.get('merged_entities'):
        output_data['merged_entities'] = merged_entities

    if args.get('all_merged_entities'):
        output_data['all_merged_entities'] = all_merged_entities

    dump_json(output_data, filename)

# Print to stdout.
if args.get('print'):

    if args.get('entities'):
        print '\nENTITIES'
        for token in entities:
            pprint(token)

    if args.get('all_entities'):
        print '\nALL ENTITIES'
        for token in all_entities:
            pprint(token)

    if args.get('merged_entities'):
        print '\nMERGED ENTITIES'
        for token in merged_entities:
            pprint(token)

    if args.get('all_merged_entities'):
        print '\nALL MERGED ENTITIES'
        for token in all_merged_entities:
            pprint(token)