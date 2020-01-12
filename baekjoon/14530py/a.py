x,y=map(int,input().split())
s,c=0,1
while True:
    if c<0 and y<=x and y>=x-abs(c) or c>0 and y>=x and y<=x+abs(c) :
        s+=abs(x-y)
        print(s)
        break
    c*=-2
    s+=abs(c)
