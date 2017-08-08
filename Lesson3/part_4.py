# part 4

name_x = ['Mikola', 'David', 'Oleg', 'Rostislav', 'Kevin', 'Tomash']
for nx in name_x:
    print(nx)

# range
print('\n-- range')
for i in range(4, 9):
    print(i, end=' ')
print()
for i in range(1, 20, 2): # range(start, end, step)
    print(i, end=' ')
print()

#
print('\n-- list')
numbers =list(range(7, 20))
print(numbers)

# for
# викоритсання циклу для створення списків ------------------ ***
print('\n-- for .. list')
num_list = [value**2 for value in range(1, 9)]
print(num_list)
num_list = [value+3 for value in range(4, 12)]
print(num_list)
num_list = [value/2 for value in range(2, 11)]
print(num_list)

#
print('\n-- copy list')
l1 = ['asd', 'klo', 'hgf', 'bnm', 'rty', 'qwe',]
l_cop1 = l1[:]
l_cop2 = l1[:2]
l_cop3 = l1[3:]
print(l1)
print(l_cop1)
print(l_cop2)
print(l_cop3)

#tuple
print('\n-- tuple')
tuple_1  = (3, 67, 9, 12, 87)
print(tuple_1)
tuple_1  = (4, 6, 12, 43)
print(tuple_1)
