n=int(input())
c=1
while True:
    if (n-1)%8==0:
        break
    n-=1
    c+=1
if c > 5:
    c=10-c
print(c)
