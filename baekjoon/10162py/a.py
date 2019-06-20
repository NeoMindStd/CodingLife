n = int(input())

a, b, c = 300, 60, 10
if  n%c!=0:
    print(-1)
else:
    print(n//a, (n%a)//b, (n%b)//c)
