import re
import json

#Define regex params
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose 
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
html_tags = r'<[^>]+>'
mentions = r'(?:@[\w_]+)'
hash_tags = r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)"
urls = r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
numbers = r'(?:(?:\d+,?)+(?:\.?\d+)?)'
words_special = r"(?:[a-z][a-z'\-_]+[a-z])"


regex_str = [
    emoticons_str,
    html_tags,
    mentions,
    hash_tags,
    urls,
    numbers,
    words_special,
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


with open('MoodVenezuela.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        print (tokens)
        
