import sys;read=sys.stdin.readline
while True:
    a,b,c,d=map(int,read().split())
    if a==b==c==d==0:break
    print(c-b,d-a)
