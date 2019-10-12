filename = 'foo'

with open(filename) as file:
    print(type(file))

    content = file.read()
    print(type(content))
    print(content)
