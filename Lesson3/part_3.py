# list
print('-- LIST -------------------------')
bicycles = ['trek', 'connndole', 'rotor', 'cube', 'Tomagavk', 'bilexus']
print(bicycles[1].title())

# add
bicycles.append('koruti')
print(bicycles)

# insert
bicycles.insert(1, 'moto')
print(bicycles)

#del
del bicycles[3]
print(bicycles)

#remove
print('-- remove')
bicycles.remove('cube')
print(bicycles)

# sort
print('-- sort')
bicycles = ['trek', 'connndole', 'rotor', 'cube', 'tomagavk', 'bilexus']
print(bicycles)
bicycles.sort()
print(bicycles)

#
print('-- sorted')
numbers = [1, 3, 6, 2, 67, -2, 7, 11]
n1 = sorted(numbers)
print(n1)
n1 = len(numbers)
print(n1)
