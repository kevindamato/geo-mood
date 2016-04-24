import json

with open('MoodVenezuela.json', 'r') as f:
    line = f.readline()
    tweet = json.loads(line)
    print(json.dumps(tweet, indent=4))
