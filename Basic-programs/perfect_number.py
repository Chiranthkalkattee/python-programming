number1 = int(input("Enter the number :"))

def perfect_number(num1):
    total = 0
    for i in range(1,num1):
        if num1%i == 0:
            total = total + i

    if total == num1:
        return "Perfect number:",number1
    else:
        return "Not a Perfect number:",number1
    
print(perfect_number(number1))


