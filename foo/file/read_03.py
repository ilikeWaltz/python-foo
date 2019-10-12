filename = 'foo'

with open(filename) as file:
    lines = file.readlines()

print(type(lines))

for l in lines:
    print(l.rstrip())
