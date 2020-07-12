import math
a,b=map(float,input().split())
c,d=map(float,input().split())
print('Slice of pizza' if a/b>c*c*math.pi/d else 'Whole pizza')
