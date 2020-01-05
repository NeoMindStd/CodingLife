import sys;read=sys.stdin.readline
n,m=map(int,read().split())
d=t=dict()
for i in range(1,n+1):
    d[i]=read()
    t[d[i]]=str(i)
r=[]
for i in range(m):
    s=read()
    try:
        s=int(s)
        r.append(d[s][:-1])
    except:r.append(t[s])
print('\n'.join(r))
