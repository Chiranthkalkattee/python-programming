def read_file():
    try:
        with open("File_Handlings/name.txt","r") as file:
            content = file.read()
            return content.split()
    except FileNotFoundError:
        return "file not found"
    

print(read_file())