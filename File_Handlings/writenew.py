def write_new_line(name):
    try:
        with open("File_Handlings/name.txt","w") as file:
            file.write("name")
            file.writelines(name)
            file.close()
    except FileNotFoundError as e:
        return e
    

print(write_new_line('chiranth'))
