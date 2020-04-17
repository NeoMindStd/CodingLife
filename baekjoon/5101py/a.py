import sys
read=sys.stdin.readline
while True:
    a,b,c=map(int,read().split())
    if a==b==c==0:
        break
    else:
        t=abs((c-a)//b)
        if (c-a)%b != 0 or a+t*b!=c: print('X')
        else: print(t+1)
