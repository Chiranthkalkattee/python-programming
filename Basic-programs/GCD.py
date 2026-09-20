# Greatest common divisor

number_one = int(input("\n Enter the 1st number:"))
number_two = int(input("\n Enter the 2nd number:"))

print("Number 1: ",number_one)
print("Number 2: ",number_two)

def gcd(number1,number2):
    if number1 ==0:
        return number2
    if number2==0:
        return number2
    if number1==number2:
        return number1
    if number1>number2:
        one = number1-number2
        return gcd(one,number2)
    else:
        sec = number2-number1
        return gcd(number1,sec)
    
response = gcd(number_one,number_two)

print("\n Greatest common divisor for ", number_one,number_two," is", response)
