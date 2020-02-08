import sys;read=sys.stdin.readline
l=[list(map(int,read().split()))for _ in range(3)]
for i in range(100):
    s,d=i%3,(i+1)%3
    l[d][1]+=l[s][1]
    t=max(l[d][1]-l[d][0],0)
    l[d][1]-=t
    l[s][1]=t
print('\n'.join(map(lambda x:str(x[1]),l)))
