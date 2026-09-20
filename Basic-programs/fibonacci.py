fib_num = int(input("\n Enter number of fibonacci element to display:"))
print("First ",fib_num," fibonacci element to display:")
i, j = 0,1
print("fibonacci element are:",i,j,end=(" "))
for m in range(2,fib_num):
    k = i+j
    i = j
    j = k
    print(k, end=(" "))

print()
