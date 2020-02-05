import sys;read=sys.stdin.readline
while True:
    x=float(input())
    if x==0:break
    n,s=1,0
    while True:
        if s>=x:break
        n+=1
        s+=1/n
    print(n-1,'card(s)')
