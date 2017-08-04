# list
shoplist = ['apple', 'lemon', 'pateto', 'banano']
print('List length = ', len(shoplist))
for item in shoplist:
    print(item, end=' | ')
shoplist.append('rise')
print('\nList = ', shoplist)
shoplist.sort()
print('\nList sort = ', shoplist)

# tuple
print('---------------- tuple')
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))

# dictionary
print('-------------------- list')
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])
# Deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

#sequence
print('----------------------- sequence')
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

#set
print('----------------------------- set')
bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

# references
print('-------------------------------- reference')
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
