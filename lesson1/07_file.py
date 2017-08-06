import os

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

name_dir = 'file\\'
# Create target directory if it is not present
if not os.path.exists(name_dir):
    os.mkdir(name_dir)  # make directory
    print('DIR - make\n')
else:
    print('DIR - ok!\n')

# Open for 'w'riting
f = open(name_dir + 'poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open(name_dir + 'poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The `line` already has a newline
    # at the end of each line
    # since it is reading from a file.
    print(line, end='')
# close the file
f.close()