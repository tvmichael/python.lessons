# dictionary
alien1 = {'color': 'white', 'age':38 , 'weight':67}
print('color= ', alien1['color'])
print(alien1)

alien1['salary'] = 4400;
print(alien1)

alien1['age'] = 39
print(alien1)

del alien1['color']
print(alien1)

#
print()
worker = {
    'Jon1': 12,
    'Modi': 23,
    'Tery': 1,
    'Ros': 34,
    'Klark': 74,
    'Erik': 33,
    'Ludvig': 87
}
print(worker)
for key, value in worker.items():
    print('Worker %s.' %key, ' standing {0} month'.format(value))

#
print('\n -- sorted')
for name in sorted(worker.keys()):
    print('Name: {0}.'.format(name))

# list-list
print('-- list-dictionari')
l1 = {'key':34, 'left': 6, 'right': 12}
l2 = {'key':34, 'left': 6, 'right': 12}
l3 = {'key':34, 'left': 6, 'right': 12}

l_dic = {'l1':l1, 'l2':l2, 'l3':l3}
l_list = [l1, l2, l3]
print(l_dic)
print(l_list,'\n')
for i in l_dic.values():
    print(i)

# create list
l1 = []
for i in range(20):
    l_new = {'x':2, 'y':3, 'z':4}
    l1.append(l_new)
print(l1)


# list in dictionary
print('\n -- list in dictionary ')
dic1 = {
    'k1': ['1', '2', 3],
    's': ['string1', 'string2'],
    'num':[11, 22]
}
for key , list_key in dic1.items():
    print('fild {0}: '.format(key), end=' ')
    for i in list_key:
        print('[', i, ']', end=' ')
    print()
