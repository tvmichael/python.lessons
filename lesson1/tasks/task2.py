#task2
import os
import time

#1. file
source = ['C:\\Temp\\python', 'C:\\Temp\\file']
#2. arhive
target_dir = 'C:'+ os.sep +'Temp'+ os.sep +'arhive'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

#3.
#4.
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y-%m-%d')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# The current time is the name of the zip archive.
now = time.strftime('%H-%M-%S')
target = today + os.sep + now + '.zip'

#5.
#zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))
zip_command = '7z a {0} {1}'.format(target, ' '.join(source))
print(source, '\n', target_dir, '\n', target, '\n', zip_command)

print('... start ........')
if os.system(zip_command) == 0:
    print('Arhived to:', target)
else:
    print('error')
print('... end.')
