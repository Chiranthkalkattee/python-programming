number = input("\n Enter the number to be reversed:")
print("\n Number to be reversed:", number)
reverse_number = ""
for i in number:
    reverse_number = i + reverse_number
print("\n Number reversed using loop:", reverse_number)
print("\n Number reversed using list slicing technique:", number[::-1])
