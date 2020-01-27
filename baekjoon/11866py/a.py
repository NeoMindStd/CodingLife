n,k=map(int,input().split())
l,r,i=[i for i in range(1,n+1)],[],k-1
while True:
    r.append(l[i])
    del l[i]
    if not l:break
    i+=k-1
    i%=len(l)
print('<'+', '.join(map(str,r))+'>')
