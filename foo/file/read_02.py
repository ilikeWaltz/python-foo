filename = 'foo'

with open(filename) as file:
    for l in file:
        print(l.rstrip())
