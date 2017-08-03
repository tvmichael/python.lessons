# if
print('Name:',end=' ')
name = 'mik'
if name == 'mik':
    print('OK')
else:
    print('Bed')

#while
print('---------------- While')
n1=4
while n1 <= 7:
    print(n1)
    n1 += 1
print('end while')

#for
print('---------------- For')
n1 = 2
n2 = 9
for i in range(n1, n2):
    print(i)
print('end for')

print('---r2')
r1 = [11, 21, 30, 4, 5]
r2 = (2, 5, 8, 9, 15)
for i in r2:
    print(i)
print('---r1')
print(r1.__len__())
for i in range(r1.__len__()):
    print('i=', i)
    print('r1=', r1[i])

# end
print('end!')