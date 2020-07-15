w,h,x,y,p=map(int,input().split())

def ccw(a,b,c):
    v=(a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
    try: return v//abs(v)
    except ZeroDivisionError: return 0

def isInCircle(c, r, p):
    return r**2 >= (c[0]-p[0])**2+(c[1]-p[1])**2

a,b,c,d=(x,y),(x+w,y),(x+w,y+h),(x,y+h)
c1,c2=(x,y+h//2),(x+w,y+h//2)

ans = 0
for i in range(p):
    pos=tuple(map(int,input().split()))
    isInRect = ccw(a,b,pos)>-1 and ccw(b,c,pos)>-1 and ccw(c,d,pos)>-1 and ccw(d,a,pos)>-1
    isInC1 = isInCircle(c1, h//2, pos)
    isInC2 = isInCircle(c2, h//2, pos)
    if isInRect or isInC1 or isInC2: ans+=1
print(ans)
