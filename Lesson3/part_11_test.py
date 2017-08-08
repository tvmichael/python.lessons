from part_11 import  get_format_name
#
print("Enter q at any time to quit")
while True:
    first = input('1: ')
    if first == 'q':
        break
    last = input('2: ')
    if last == 'q':
        break
    fn = get_format_name(first, last)
    print('\t formatted: ', fn)
