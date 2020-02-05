import sys;read=sys.stdin.readline
a,b,x,y=map(int,read().split())
print(min(abs(a-b),abs(a-x)+abs(b-y),abs(a-y)+abs(b-x)))
