import json

filename = 'foo.json'
with open(filename) as f:
    data = json.load(f)

print(data)
print(type(data))
