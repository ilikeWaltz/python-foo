import json

d = dict()
d['k'] = 'v'

filename = 'foo.json'
with open(filename, 'w') as f:
    json.dump(d, f)
