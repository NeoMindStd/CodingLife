import sys;read=sys.stdin.readline
l=[]
for T in range(int(read())):
    n=int(read())
    l.append(f'{n*(n+1)//2} {n*n} {n*(n+1)}')
print('\n'.join(l))
