import os
import sys
files =os.listdir(".")
a=sys.argv[1]
if os.path.exists(a):
    os.mk(a)
    print('Successfully removed the folder named',a)
else:
    print('No Folder already exists')
print(files)
b=sys.argv[2]
if os.path.exists(b):
    os.remove(b)
    print("File successfully deleted")
else:
    print("No",b,"file exists")