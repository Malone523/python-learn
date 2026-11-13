import os

file_path = "data/test.txt"

if os.path.exists(file_path):
    print(f"Location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
        
else:
    print("That location doess not exist")