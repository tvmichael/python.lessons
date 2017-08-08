#file

#read file
with open('pi_digits.txt') as file_object:
    contents =file_object.read()
    print(contents)

# виводимо по рядках
print('-- 1')
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip(), end=' ')

# зберігаємо дані з файлу до списку
print('\n\n-- 2')
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
#
pi_string = ''
for line in lines:
    pi_string +=line.strip()

print(pi_string)
print(pi_string[:15])
print('len=', len(pi_string))

# пошук входження послідовності цифр
contents = None
try:
    with open('_pi1000000.txt') as file_object:
        contents = file_object.read()
        nf ='050979'
        if nf in contents:
            print('Yes')
        else:
            print('No')
except FileNotFoundError:
    print('File not found')

# json
import json
print('-- json')
tuple = (5, 7, 8, 12, 89, 123, 546)
numbers = [2, 5, 7, 9, 2, 6, 4, 0, 1, 7, 14, 21]
list1 = [4.4, 5.7, 12.7]
dic1 = {'d1':list1, 'd2':numbers, 'tuple':tuple}
file_name = 'number.json'
with open(file_name, 'w') as file_object:
    json.dump(dic1, file_object)

dic2 = None
with open(file_name, 'r') as file_object:
    dic2 = json.load(file_object)
print(dic2)