l=sorted(map(int,input().split()))
a,b=l[1]-l[0],l[2]-l[1]
if a>b:print((l[1]+l[0])//2)
elif a<b:print((l[2]+l[1])//2)
else:print(l[2]+a)
