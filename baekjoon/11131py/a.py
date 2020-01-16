import sys;read=sys.stdin.readline
for T in range(int(read())):
    read()
    s=sum(map(int,read().split()))
    if s>0:r='Right'
    elif s<0:r='Left'
    else:r='Equilibrium'
    print(r)
