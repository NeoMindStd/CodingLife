n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

d=dict()
for i in a:
    try:d[i]+=1
    except:d[i]=1
r=[]
for i in b:
    try:r.append(d[i])
    except:r.append(0)
print(' '.join(map(str,r)))
