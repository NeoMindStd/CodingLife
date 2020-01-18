import sys;read=sys.stdin.readline
for T in range(int(read())):
    a,b,c,d,e,f=map(int,read().split())
    print(abs(a-d)+abs(b-e)+c+f)
