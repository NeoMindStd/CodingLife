import sys;read=sys.stdin.readline
l=[]
for T in range(int(read())):
    t,n=map(int,read().split())
    l.append(f'{t} {n*(n+1)//2} {n*n} {n*(n+1)}')
print('\n'.join(l))
