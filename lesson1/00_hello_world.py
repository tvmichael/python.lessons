print('Hello World')

# first program
print(1.23)
age = 38.123456789
num = 11
#int(input('num = '))
name = 'Michael'
print(age, name)
print('Age: {0:.3}  Name:{1}'.format(age,name))
if num == 10:
    print(num)
else:
    print('Num>10')
print('END')

#while
while num <= 25:
    print(num)
    num +=1

import sys
print (tuple(sys.version_info))

# all keywords
import keyword
print(keyword.kwlist)

#list
list1 = [1,2,3,4,5,6,7,8,9,0]
print(list1)
print(type(list1))

# arr1
print('------- arr1')
arr1 = [2,45,6,8,77]
arr1[1]=111
print(arr1)
i = iter(arr1)
print(i.__next__())
print(i.__next__())
print(next(i))

# next
print('------- next')
for i in arr1:
    print(i)

#str
print('------- str')
for i in 'word':
    print(i + '-', end=' ')
    print()

#dictionary
dictionary = {'x':11, 'y':12, 'z':13}
for key in dictionary:
    print(key, '=', dictionary[key], end=' ')

print()
x, y, z  = [1, 2, 3]
print(x)
print(y)
print(z)

# type
print('------- object')
obj1 = bytes('String1', 'utf-8', 'errors obj1')
obj2 = bytes('String2', 'utf-8')
print(type(obj1))
print(obj1)