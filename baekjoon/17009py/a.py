a,b=sum([int(input())*(3-i) for i in range(3)]),sum([int(input())*(3-i) for i in range(3)])
if a>b:
    print("A")
elif a<b:
    print("B")
else:
    print("T")
