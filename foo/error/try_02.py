filename = "../file/foo"

try:
    with open(filename) as f:
        lines = f.readlines()
except FileNotFoundError:
    print("file not found.")
else:
    print(lines)