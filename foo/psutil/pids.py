import psutil

# pids
ids = psutil.pids()

#
for i in ids:
    try:
        p = psutil.Process(i)
        n = p.name()
        print("pid: " + str(i) + ", name: " + p.name())
    except ProcessLookupError:
        print("pid err" + i)
