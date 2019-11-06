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

l1,l2,l3=list(map(int, input().split())),list(map(int, input().split())),list(map(int, input().split()))
print(ccw([*l1],[*l2],[*l3]))
