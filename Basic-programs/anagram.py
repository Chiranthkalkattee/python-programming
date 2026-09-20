string_one = input("\n enter the first string: ")
string_two = input("\n enter the secong string: ")

# print(string_one)
# print(string_two)
# str_one = "part"
# str_two = "trcp"


def anagram(str_one,str_two):
    if len(str_one) == len(str_two):
        str1 = sorted(str_one)
        str2 = sorted(str_two)

        if str1 == str2:
            return "Given string is anagram", str_one,str_two
        else:
            return "Given string is Not a anagram", str_one,str_two
    return "Given string is Not a anagram", str_one,str_two
    

print(anagram(string_one,string_two))


# if len(str_one) == len(str_two):
#     for i in str_one:
#         # print(i)
#         if i  in str_two.split(','):
#             print(i)
#         print("Given string is anagram", str_one,str_two)
#     print("Given string is Not a anagram", str_one,str_two)
