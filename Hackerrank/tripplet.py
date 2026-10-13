a1 = list(map(int, input().rstrip().split()))
b1 = list(map(int, input().rstrip().split()))


def tripplet(a,b):
    al = 0
    bl = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            al+=1
        elif a[i] < b[i]:
            bl+=1
            
    return [al,bl]

print(tripplet(a1,b1)) 