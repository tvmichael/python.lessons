import os
import time
import zipfile

# file directory
source = ['C:\\Temp\\python', 'C:\\Temp\python\\file']
# main backup directory
target_dir = 'C:' + os.sep + 'Temp' + os.sep + 'backup'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    print('Not exists', target_dir)
    os.mkdir(target_dir)  # make directory

# in the main directory.
today_dir = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
file_name = time.strftime('%H%M%S')+'.zip'

# zip file name
zip_file = today_dir + os.sep + file_name
zip_file = target_dir + os.sep + 'backup.zip'
print(zip_file)

#zpf = zipfile.ZipFile(zip_file, mode='w', compression=zipfile.ZIP_DEFLATED, allowZip64=True)

#
#
#
import glob
# open the zip file for writing, and write stuff to it
print('\n')
d_1 = "C:\\Temp\\backup"
f_1 = d_1 + "\\test.zip"
print(f_1, ' -- ', d_1)
file = zipfile.ZipFile(f_1, "w")

for name in glob.glob("C:\\Temp\\file\\*"):
    print(name)
    file.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
file.close()

# open the file again, to see what's in it
file = zipfile.ZipFile(f_1, "r")
for info in file.infolist():
   print(info.filename, info.date_time, info.file_size, info.compress_size)



