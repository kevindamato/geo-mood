import operator
import json
import string
from tokenize_tweet import preprocess
from collections import Counter
from nltk.corpus import stopwords

punctuation = list(string.punctuation)
stop = stopwords.words('spanish') + punctuation + ['RT', 'via', 'SE', 'LA', '…']

with open('MoodVenezuela.json', 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_all = [term for term in preprocess(tweet['text']) if term not in stop]
        count_all.update(terms_all)
    print(count_all.most_common(5))
