import json

d = dict()
d['k'] = 'v'

json_str = json.dumps(d)

print(json_str)
print(type(json_str))
