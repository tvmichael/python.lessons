#task1
print('Task 1 --------------------------------------------\n')
import os
import time

#1. file
source = ['C:\\Temp\\python', 'C:\\Temp\\file']
#2. arhive
target_dir = 'C:\\Temp\\arhive'

#3.
#target = target_dir + os.sep + time.strftime('%Y%m%d')+'-'+ time.strftime('%H%M%S')+'.zip'
target = target_dir + os.sep + time.strftime('%Y%m%d-%H%M%S')+'.zip'
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

#import subprocess
# v1
#PIPE = subprocess.PIPE
#proc = subprocess.Popen(zip_command, shell = True)
#v2
#proc = subprocess.Popen(zip_command, shell=True, stdout=subprocess.PIPE)
#print('proc: ', proc)

