#
motorcycles = ['honda', 'yamaha']
print(motorcycles)

# append
motorcycles.append('suzuki')
print(motorcycles)

# pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)

# insert
motorcycles.insert(0, 'suzuki')
print(motorcycles)

# del
del motorcycles[0]
print(motorcycles)

# pop(i)
first_owned = motorcycles.pop(1)
print(motorcycles)

# remove(k), if k not exists, throw a ValueError
k = 'yamaha'
try:
    motorcycles.remove(k)
    print(motorcycles)
except ValueError:
    print(k + " not exist!")

# update
motorcycles.append(k)
motorcycles[0] = 'bmw'
print(motorcycles)
