
# if
print('-- if')
cars = ['audi', 'bmw', 'honda', 'reno', 'fiat', 'lexus']
for car in cars:
    if car == 'reno':
        print(car.upper())
    else:
        print(car.lower())

#
print('\n-- if .. and')
a1, b1, c1 = 1, 2, 3
if a1 == 1 and b1 == 2 and c1 ==3:
    print(a1, b1, c1)
else:
    print('False')


# entry in list
print('\n-- entry in list')
res1 = 'honda' in cars
print(res1)
res1 = 'volvo' in cars
print(res1)

car = 'volvo'
if car not in cars:
    print("car 'volvo' absent")