import sys;read=sys.stdin.readline
n,p,h=map(int,read().split())
r=[]
for T in range(n):
    x=int(read())
    if p>x:r.append(f'NTV: Dollar dropped by {p-x} Oshloobs')
    elif h<x:
        r.append(f'BBTV: Dollar reached {x} Oshloobs, A record!')
        h=x
    p=x
print('\n'.join(r))
