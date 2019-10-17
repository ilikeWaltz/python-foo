#
motorcycles = ['honda', 'yamaha', 'bmw', 'suzuki']
print(motorcycles)

# pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)

# pop(i)
popped_motorcycle = motorcycles.pop(1)
print(motorcycles)

# del
del motorcycles[0]
print(motorcycles)

# remove(k), if k not exists, throw a ValueError
k = 'yamaha'
try:
    motorcycles.remove(k)
    print(motorcycles)
except ValueError:
    print(k + " not exist!")
