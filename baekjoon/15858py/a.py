a,b,c=map(int,input().split())
i = 0
a*=b
result = (str(a//c)+".")
d = a%c
while i < 1000:
    d *= 10
    m = d//c
    result += str(m)
    d %= c
    if d == 0:
        break
    i += 1
print(result)
