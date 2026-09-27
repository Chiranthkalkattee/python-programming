import os

def file_exists(filename):
    if os.path.exists(filename):
        return "file found"
    else:
        return "file not found"
    

print(file_exists("File_Handlings/name.txt"))
