n=int(input())
a=dict()
for c in input():
    try:a[c]+=1
    except:a[c]=1
s=0
for i in range(n-1):
    b=dict(a)
    for c in input():
        try:b[c]-=1
        except:b[c]=-1
    l=b.values()
    m,M=10,-10
    c=C=0
    for p in l:
        m=min(p,m)
        M=max(p,M)
        if p==-1:c+=1
        if p==1:C+=1
    if m>-2 and M<2 and c in[0,1] and C in[0,1]:s+=1
print(s)
