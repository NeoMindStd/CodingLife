import sys;read=sys.stdin.readline

for T in range(int(read())):
    n,d=int(read()),{}
    for _ in range(n):
        a,b=read().split()
        try:d[b].add(a)
        except:d[b]=set([None,a])
    x=1
    for s in d.values():x*=len(s)
    print(x-1)
