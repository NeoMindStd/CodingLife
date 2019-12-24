import sys;read=sys.stdin.readline
h,m,s=map(int,read().split())
t=h*3600+m*60+s
r=[]
for T in range(int(read())):
    l=list(map(int,read().split()))
    if l[0]==3:r.append(f'{h} {m} {s}')
    elif l[0]==1:
        t+=l[1]
        t%=3600*24
        h,m,s=t//3600,t%3600//60,t%60
    else:
        t+=24*3600-l[1]
        t%=3600*24
        h,m,s=t//3600,t%3600//60,t%60
    if h==24:h=0
print('\n'.join(map(str,r)))
