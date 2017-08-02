print('Operators and expressions')
#lesson 1
print('Enter two number')
num1 = 11
num2 = 12
print('Sum: ', num1+num2)
multiple = num1 * num2
print('Multiple: ', multiple)
divide = num1/num2
print('Divide: ', divide)
power = num1**num2
print('Power: ', power)

#
x = 100
x = ~x
print(x)
x = ~x
print(x)
x = ~x
print(x)

# if
print('----------- if')
import random
n1 = int(random.random()*200)
print(n1)
n2 = int(random.random()*200)
print(n2)
if n1 > 123:
    print('sum =', n1 + n2)
else:
    print('difference =', n1 - n2)

# while
n1 = int(random.random()*10)
while n1 <= 10:
    print(n1,' | ', end=' ')
    n1 += 1
else:
    print('end while')

#for
print('-------- for')
n3 = int(random.random()*10)
for i in range(1,5):
    print(i)
else:
    print('end for!')