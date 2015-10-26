#!/usr/bin/python

import urllib2
import urllib
import json
import gzip
from StringIO import StringIO
from itertools import product, ifilterfalse
from operator import itemgetter
from config.config import BABELFY_API_URL


class BabelfyClient(object):
    """API client for the babelfy api.
    http://babelfy.org/guide
    """

    def __init__(self, api_key, params=None):
        """Initialize the BabelfyClient.

        Arguments:
        api_key -- key to connect the babelfy api

        Keyword arguments:
        params -- params for the api request
        """
        self._api_key = api_key
        self._params = params or dict()
        self._data = list()
        self._entities = list()
        self._all_entities = list()
        self._merged_entities = list()
        self._all_merged_entities = list()
        self._text = None

    @property
    def entities(self):
        """returns a list of entities received from babelfy api
        """
        if not self._entities:
            self._parse_entities()
        return self._entities

    @property
    def all_entities(self):
        """returns a list of entities received from babelfy api and all
        non-entity words from the sentence
        """
        if not self._all_entities:
            self._parse_non_entities()
        return self._all_entities

    @property
    def merged_entities(self):
        """returns a list of entities received from babelfy api merged to the
        longest possible entities
        """
        if not self._merged_entities:
            self._parse_merged_entities()
        return self._merged_entities

    @property
    def all_merged_entities(self):
        """returns a list entities received from babelfy api and all non-entity
        words from the sentence merged to the longest possible entities
        """
        if not self._all_merged_entities:
            self._parse_all_merged_entities()
        return self._all_merged_entities

    def babelfy(self, text, params=None):
        """make a request to the babelfy api and babelfy param text
        set self._data with the babelfied text as json object
        """
        self._entities = list()
        self._all_entities = list()
        self._merged_entities = list()
        self._all_merged_entities = list()
        self._text = " ".join(word.strip() for word in text.split())

        params = params or self._params
        params['key'] = self._api_key
        params['text'] = self._text
        if isinstance(params['text'], unicode):
            params['text'] = params['text'].encode('utf-8')
        url = BABELFY_API_URL + '?' + urllib.urlencode(params)

        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        self._data = json.loads(f.read())

    def _parse_entities(self):
        """enrich the babelfied data with the text an the isEntity items
        set self._entities with the enriched data
        """
        entities = list()

        for result in self._data:
            entity = dict()
            char_fragment = result.get('charFragment')
            start = char_fragment.get('start')
            end = char_fragment.get('end')
            entity[u'start'] = start
            entity[u'end'] = end
            entity[u'text'] = unicode(self._text[start: end+1])
            entity[u'isEntity'] = True
            for key, value in result.items():
                entity[key] = value
            entities.append(entity)
        self._entities = entities

    def _parse_non_entities(self):
        """create data for all non-entities in the babelfied text
        set self._all_entities with merged entity and non-entity data
        """
        def _differ(tokens):
            inner, outer = tokens
            not_same_start = inner.get('start') != outer.get('start')
            not_same_end = inner.get('end') != outer.get('end')
            return not_same_start or not_same_end

        def _get_dot_token():
            dot_token = dict()
            dot_token['start'] = (len(self._text) - 1)
            dot_token['end'] = dot_token['start']
            dot_token['text'] = '.'
            dot_token['isEntity'] = False
            return dot_token

        if self._text.endswith('.'):
            text = self._text[:-1]
            add_dot_token = True
        else:
            text = self._text
            add_dot_token = False

        index = 0
        all_tokens = list()
        for token in text.split():

            comma_token = False
            if token.endswith(','):
                comma_token = True
                token = token[:-1]

            start = index
            end = (start + len(token))
            index += (len(token) + 1)

            all_tokens.append({
                'start': start,
                'end': end - 1,
                'text': self._text[start: end],
                'isEntity': False,
            })

            if comma_token:
                all_tokens.append({
                    'start': index,
                    'end': index,
                    'text': ',',
                    'isEntity': False,
                })
                index += 1

        token_tuples = list(product(all_tokens, self.entities))
        redundant = [
            tokens[0] for tokens in token_tuples if not _differ(tokens)]
        non_entity_tokens = [
            item for item in all_tokens if item not in redundant]

        if add_dot_token:
            non_entity_tokens.append(_get_dot_token())

        self._all_entities = sorted(
            self._entities + non_entity_tokens, key=itemgetter('start'))

    def _parse_merged_entities(self):
        """set self._merged_entities to the longest possible(wrapping) tokens
        """
        self._merged_entities = list(ifilterfalse(
            lambda token: self._is_wrapped(token, self.entities),
            self.entities))

    def _parse_all_merged_entities(self):
        """set self._all_merged_entities to the longest possible(wrapping)
        tokens including non-entity tokens
        """
        self._all_merged_entities = list(ifilterfalse(
            lambda token: self._is_wrapped(token, self.all_entities),
            self.all_entities))

    def _wraps(self, tokens):
        """determine if a token is wrapped by another token
        """
        def _differ(tokens):
            inner, outer = tokens
            not_same_start = inner.get('start') != outer.get('start')
            not_same_end = inner.get('end') != outer.get('end')
            return not_same_start or not_same_end

        def _in_range(tokens):
            inner, outer = tokens
            starts_in = outer.get('start') <= inner.get('start') \
                <= outer.get('end')
            ends_in = outer.get('start') <= inner.get('end') \
                <= outer.get('end')
            return starts_in and ends_in

        if not _differ(tokens):
            return False

        return _in_range(tokens)

    def _is_wrapped(self, token, tokens):
        """check if param token is wrapped by any token in tokens
        """
        for t in tokens:
            is_wrapped = self._wraps((token, t))
            if is_wrapped:
                return True
        return False
