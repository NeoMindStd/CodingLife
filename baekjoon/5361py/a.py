import sys;read=sys.stdin.readline
p=[350.34,230.9,190.55,125.3,180.9]
for T in range(int(read())):
    l=list(map(int,read().split()))
    s=0
    for i in range(len(l)):s+=p[i]*l[i]
    print('$%.2f'%s)
