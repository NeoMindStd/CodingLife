a1,a2,b1,b2,c1,c2=map(int,input().split())
a,b,c=(a1,a2),(b1,b2),(c1,c2)

def ccw(a,b,c): 
    v=(a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*a[0]) 
    try: return v//abs(v) 
    except ZeroDivisionError: return 0 

if ccw(a,b,c) == 0: print(-1)
else:
    A=((a[0]-b[0])**2+(a[1]-b[1])**2)**.5
    B=((b[0]-c[0])**2+(b[1]-c[1])**2)**.5
    C=((c[0]-a[0])**2+(c[1]-a[1])**2)**.5
    l=sorted([2*A+2*B,2*B+2*C,2*C+2*A])
    print(l[2]-l[0])
