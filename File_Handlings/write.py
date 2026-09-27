# Write a Python program that accepts a user’s name as input and writes it to a file called user.txt.

name = input("Enter the name:")

def write_file(name):
    try:
        with open("File_Handlings/name.txt", "w") as file:
            file.write(name)
    except FileNotFoundError:
        return "file not found"
    

def append_file(name):
    try:
        with open("File_Handlings/name.txt", "a") as file:
            file.writelines(name)
    except FileNotFoundError:
        return "file not found"
    

print(append_file(name))