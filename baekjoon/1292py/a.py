import math
a,b=map(int, input().split())
x=math.ceil(((1+8*a)**.5-1)/2)
y=math.ceil(((1+8*b)**.5-1)/2)
if x==y:print((b-a+1)*x)
else:    
    s=x*(x*(x+1)//2-a+1)
    for i in range(x+1,y): s+=i*i
    s+=y*(b-y*(y-1)//2)
    print(s)
