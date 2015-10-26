import unittest
import json
from babelfy import BabelfyClient
from config.config import API_KEY, LANG
from reader import read_txt_file
import os

params = dict()
params['lang'] = LANG
bc = BabelfyClient(API_KEY, params)
txt = "BabelNet is both a multilingual encyclopedic dictionary and a semantic network."
entities = [
    {
        "tokenFragment":{"start":0,"end":0},
        "charFragment":{"start":0, "end":7},
        "babelSynsetID":"bn:03083790n",
        "DBpediaURL":"http://dbpedia.org/resource/BabelNet",
        "BabelNetURL":"http://babelnet.org/rdf/s03083790n",
        "score":1.0,
        "coherenceScore":0.6666666666666666,
        "globalScore":0.11428571428571428,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":4,	"end":4},
        "charFragment":{"start":19,	"end":30},
        "babelSynsetID":"bn:00010388n",
        "DBpediaURL":"http://dbpedia.org/resource/Multilingualism",
        "BabelNetURL":"http://babelnet.org/rdf/s00010388n",
        "score":0.9,
        "coherenceScore":0.5,
        "globalScore":0.06428571428571428,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":5,	"end":5},
        "charFragment":{"start":32,	"end":43},
        "babelSynsetID":"bn:00102202a",
        "DBpediaURL":"",
        "BabelNetURL":"http://babelnet.org/rdf/s00102202a",
        "score":0.0,
        "coherenceScore":0.0,
        "globalScore":0.0,
        "source":"MCS"
    },{
        "tokenFragment":{"start":5,	"end":6},
        "charFragment":{"start":32,	"end":54},
        "babelSynsetID":"bn:02290297n",
        "DBpediaURL":"http://dbpedia.org/resource/Encyclopedic_dictionary",
        "BabelNetURL":"http://babelnet.org/rdf/s02290297n",
        "score":1.0,
        "coherenceScore":0.3333333333333333,
        "globalScore":0.02857142857142857,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":6,	"end":6},
        "charFragment":{"start":45,	"end":54},
        "babelSynsetID":"bn:00026967n",
        "DBpediaURL":"http://dbpedia.org/resource/Dictionary",
        "BabelNetURL":"http://babelnet.org/rdf/s00026967n",
        "score":0.9130434782608695,
        "coherenceScore":1.0,
        "globalScore":0.3,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":9,	"end":9},
        "charFragment":{"start":62,	"end":69},
        "babelSynsetID":"bn:00110347a",
        "DBpediaURL":"",
        "BabelNetURL":"http://babelnet.org/rdf/s00110347a",
        "score":1.0,
        "coherenceScore":0.16666666666666666,
        "globalScore":0.007142857142857143,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":9,	"end":10},
        "charFragment":{"start":62,	"end":77},
        "babelSynsetID":"bn:02275757n",
        "DBpediaURL":"http://dbpedia.org/resource/Semantic_network",
        "BabelNetURL":"http://babelnet.org/rdf/s02275757n",
        "score":1.0,
        "coherenceScore":0.5,
        "globalScore":0.08571428571428572,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":10, "end":10},
        "charFragment":{"start":71,	"end":77},
        "babelSynsetID":"bn:00057379n",
        "DBpediaURL":"",
        "BabelNetURL":"http://babelnet.org/rdf/s00057379n",
        "score":0.0,
        "coherenceScore":0.0,
        "globalScore":0.0,
        "source":"MCS"
    }
]

merged_entities = [
    {
        "tokenFragment":{"start":0,"end":0},
        "charFragment":{"start":0, "end":7},
        "babelSynsetID":"bn:03083790n",
        "DBpediaURL":"http://dbpedia.org/resource/BabelNet",
        "BabelNetURL":"http://babelnet.org/rdf/s03083790n",
        "score":1.0,
        "coherenceScore":0.6666666666666666,
        "globalScore":0.11428571428571428,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":4,	"end":4},
        "charFragment":{"start":19,	"end":30},
        "babelSynsetID":"bn:00010388n",
        "DBpediaURL":"http://dbpedia.org/resource/Multilingualism",
        "BabelNetURL":"http://babelnet.org/rdf/s00010388n",
        "score":0.9,
        "coherenceScore":0.5,
        "globalScore":0.06428571428571428,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":5,	"end":6},
        "charFragment":{"start":32,	"end":54},
        "babelSynsetID":"bn:02290297n",
        "DBpediaURL":"http://dbpedia.org/resource/Encyclopedic_dictionary",
        "BabelNetURL":"http://babelnet.org/rdf/s02290297n",
        "score":1.0,
        "coherenceScore":0.3333333333333333,
        "globalScore":0.02857142857142857,
        "source":"BABELFY"
    },{
        "tokenFragment":{"start":9,	"end":10},
        "charFragment":{"start":62,	"end":77},
        "babelSynsetID":"bn:02275757n",
        "DBpediaURL":"http://dbpedia.org/resource/Semantic_network",
        "BabelNetURL":"http://babelnet.org/rdf/s02275757n",
        "score":1.0,
        "coherenceScore":0.5,
        "globalScore":0.08571428571428572,
        "source":"BABELFY"
    }
]

non_entities = [
    {
        u'isEntity': False,
        u'start': 9,
        u'end': 10,
        u'text': 'is',
    },
    {
        u'isEntity': False,
        u'start': 12,
        u'end': 15,
        u'text': u'both',
    },
    {
        u'isEntity': False,
        u'start': 17,
        u'end': 17,
        u'text': u'a',
    },
    {
        u'isEntity': False,
        u'start': 56,
        u'end': 58,
        u'text': u'and',
    },
    {
        u'isEntity': False,
        u'start': 60,
        u'end': 60,
        u'text': u'a',
    },
    {
        u'isEntity': False,
        u'start': 78,
        u'end': 78,
        u'text': u'.',
    },
]


class BabelfyTestCase(unittest.TestCase):

    def test_read_text(self):
        root = os.path.abspath(os.path.dirname(__file__))
        text_path = os.path.join(root, 'txt')
        read = read_txt_file(text_path)
        self.assertTrue(self, read == txt)

    def test_data(self):
        """test response data
        """
        data = json.loads(json.dumps(entities))
        bc.babelfy(txt)

        data.sort(key=lambda x: x['tokenFragment']['start'], reverse=False)
        bc._data.sort(key=lambda x: x['tokenFragment']['start'], reverse=False)

        self.assertTrue(len(data) == len(bc._data))

        for i, token in enumerate(bc._data):
            response_token = data[i]

            self.assertTrue(token['tokenFragment'] == response_token['tokenFragment'])
            self.assertTrue(token['charFragment'] == response_token['charFragment'])

    def test_entites(self):
        """test entities
        """
        data = json.loads(json.dumps(entities))
        for token in data:
            char_fragment = token.get('charFragment')
            start = char_fragment.get('start')
            end = char_fragment.get('end')
            token['isEntity'] = True
            token[u'start'] = start
            token[u'end'] = end
            token[u'text'] = unicode(txt[start: end+1])

        bc.babelfy(txt)

        data.sort(key=lambda x: x['tokenFragment']['start'], reverse=False)
        bc.entities.sort(key=lambda x: x['tokenFragment']['start'], reverse=False)

        self.assertTrue(len(data) == len(bc._data))

        for i, token in enumerate(bc.entities):
            response_token = data[i]
            self.assertTrue(token['isEntity'] == response_token['isEntity'])
            self.assertTrue(token['start'] == response_token['start'])
            self.assertTrue(token['end'] == response_token['end'])
            self.assertTrue(token['text'] == response_token['text'])

    def test_non_entites(self):
        """test non-entities
        """
        data = json.loads(json.dumps(entities))
        for token in data:
            char_fragment = token.get('charFragment')
            start = char_fragment.get('start')
            end = char_fragment.get('end')
            token['isEntity'] = True
            token[u'start'] = start
            token[u'end'] = end
            token[u'text'] = unicode(txt[start: end+1])

        bc.babelfy(txt)
        data = data + non_entities

        data.sort(key=lambda x: x['start'], reverse=False)
        bc.all_entities.sort(key=lambda x: x['start'], reverse=False)

        self.assertTrue(len(data) == len(bc.all_entities))

        for i, token in enumerate(bc.all_entities):
            response_token = data[i]
            self.assertTrue(str(token['isEntity']) == str(response_token['isEntity']))
            self.assertTrue(str(token['start']) == str(response_token['start']))
            self.assertTrue(str(token['end']) == str(response_token['end']))
            self.assertTrue(str(token['text']) == str(response_token['text']))


    def test_merged_entites(self):
        """test entities
        """
        data = json.loads(json.dumps(merged_entities))
        for token in data:
            char_fragment = token.get('charFragment')
            start = char_fragment.get('start')
            end = char_fragment.get('end')
            token['isEntity'] = True
            token[u'start'] = start
            token[u'end'] = end
            token[u'text'] = unicode(txt[start: end+1])

        bc.babelfy(txt)

        data.sort(key=lambda x: x['start'], reverse=False)
        bc.merged_entities.sort(key=lambda x: x['start'], reverse=False)

        self.assertTrue(len(data) == len(bc.merged_entities))

        for i, token in enumerate(bc.merged_entities):
            response_token = data[i]
            self.assertTrue(token['isEntity'] == response_token['isEntity'])
            self.assertTrue(token['start'] == response_token['start'])
            self.assertTrue(token['end'] == response_token['end'])
            self.assertTrue(token['text'] == response_token['text'])

    def test_all_merged_entites(self):
        """test entities
        """
        data = json.loads(json.dumps(merged_entities))
        for token in data:
            char_fragment = token.get('charFragment')
            start = char_fragment.get('start')
            end = char_fragment.get('end')
            token['isEntity'] = True
            token[u'start'] = start
            token[u'end'] = end
            token[u'text'] = unicode(txt[start: end+1])

        bc.babelfy(txt)
        data = data + non_entities
        data.sort(key=lambda x: x['start'], reverse=False)
        bc.all_merged_entities.sort(key=lambda x: x['start'], reverse=False)

        self.assertTrue(len(data) == len(bc.all_merged_entities))

        for i, token in enumerate(bc.all_merged_entities):
            response_token = data[i]
            self.assertTrue(token['isEntity'] == response_token['isEntity'])
            self.assertTrue(token['start'] == response_token['start'])
            self.assertTrue(token['end'] == response_token['end'])
            self.assertTrue(token['text'] == response_token['text'])
