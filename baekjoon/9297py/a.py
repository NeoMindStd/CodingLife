import sys;read=sys.stdin.readline
for T in range(int(read())):
    n,d=map(int,read().split())
    r=f'Case {T+1}: '
    if n//d!=0:r+=f'{n//d} '
    if n%d!=0:r+=f'{n%d}/{d}'
    if n==0:r+='0'
    print(r)
