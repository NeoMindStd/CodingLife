n=input()
l={i:False for i in range(-1000,1001)}
a=list(map(int,input().split()))
for i in a:l[i]=True
r=[]
for i in range(-1000,1001):
    if l[i]:r.append(i)
print(*r)
