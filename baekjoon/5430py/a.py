import sys;read=sys.stdin.readline
for T in range(int(read())):
    p,n=read(),int(read())
    h,t,d=1,n,1
    l=[-1]
    if n>0:l+=list(map(int,input()[1:-1].split(',')))
    else:input()
    for c in p:
        if c=='R':h,t,d=t,h,-d
        elif c=='D':h+=d
    print(('['+','.join(map(str,l[h:t+d:d]))+']')if h*d<=(t+d)*d else'error')
