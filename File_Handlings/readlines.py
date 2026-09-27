def readlines():
    with open("File_Handlings/name.txt","r") as file:
        lines = file.readlines()
    return len(lines)

    

print(readlines())
