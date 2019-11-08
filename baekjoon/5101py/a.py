import sys
read=sys.stdin.readline
while True:
    a,b,c=map(int,read().split())
    if a==b==c==0:
        break
    elif (c-a)%b != 0:
        print('X')
    else:
        print((c-a)//b+1)
