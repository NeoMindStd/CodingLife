n,p=map(int,input().split())
a,t=[],n
while True:
    t=(t*n)%p
    if t in a:
        print(len(a)-a.index(t))
        break
    a.append(t)
