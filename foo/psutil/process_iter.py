import psutil

ps = psutil.process_iter()

for p in ps:
    print("p id: " + str(p.pid) + ", p name: " + p.name())
