import psutil

# https://psutil.readthedocs.io/en/latest/

cp = psutil.cpu_percent()
print(cp)
