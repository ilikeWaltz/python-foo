import json

numbers = list(range(0, 9))

filename = 'foo.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
