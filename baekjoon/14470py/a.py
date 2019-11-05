l=[int(input()) for _ in range(5)]
r=0
if l[0]<0:
    r+=-l[0]*l[2]
    l[0]=0
if l[0]==0:
    r+=l[3]
r+=(l[1]-l[0])*l[4]
print(r)
