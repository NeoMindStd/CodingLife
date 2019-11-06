def ccw(a, b, c):
    x1,x2,x3=a[0],b[0],c[0]
    y1,y2,y3=a[1],b[1],c[1]
    tmp=x1*y2+x2*y3+x3*y1
    tmp-=y1*x2+y2*x3+y3*x1
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

def isCross(a, b, c, d):
    ab = ccw(a,b,c)*ccw(a,b,d)
    cd = ccw(c,d,a)*ccw(c,d,b)
    if ab==cd==0:
        if a>b:
            a,b=b,a
        if c>d:
            c,d=d,c
        return c<=b and a<=d
    return ab<=0 and cd<=0

l1,l2=list(map(int, input().split())),list(map(int, input().split()))
print(1 if isCross((l1[0],l1[1]),(l1[2],l1[3]),(l2[0],l2[1]),(l2[2],l2[3])) else 0)
