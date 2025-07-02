import os
folder=input("Enter the name of the folder")
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created")