for T in range(int(input())):
    n=int(input())
    l=b=1000.0
    r=t=-1000.0
    for i in range(n):
        x,y=map(float,input().split())
        l,b,r,t=min(l,x),min(b,y),max(r,x),max(t,y)
    print('Case %d: Area %f, Perimeter %f'%(T+1,(r-l)*(t-b),2*(r-l+t-b)))
