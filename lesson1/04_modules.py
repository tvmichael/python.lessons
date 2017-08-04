# Modules

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\nThe P is', sys.path, '\n')

# name
if __name__ == '__main__':
    print('self..')
else:
    print('import..')

# imoprt module
import module_one
module_one.f_hi()
print(module_one.__version__)

print('-----------------')
first = sys.argv
print('first=', first)


print('-----------------')
n1 = 10
s1 = n1.__abs__()
s1 =n1.__add__(10)
print(s1)
