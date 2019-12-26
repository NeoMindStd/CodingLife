r=[]
n,f=int(input()),int(input())
e=o=-1
for i in range(2,n+1):
    f=(f+1)%2
    r.append(str(f))
    if i%2==0:
        if -1!=e!=f:
            r=['Love is open door']
            break
        e=f
    if i%3==0:
        if -1!=o!=f:
            r=['Love is open door']
            break
        o=f
print("\n".join(r))
