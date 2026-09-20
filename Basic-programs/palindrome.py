string1 = input("\n Enter the string to check wheather given string is palindrome are not:")

def palindrome(string_a):
    palindrome = string_a[::-1]
    print(palindrome)
    if palindrome == string_a:
        return f"Given string is a palindrome", string_a
    else:
        return f"Given stind is not a palindrome",string_a
    

print(palindrome(string1))
