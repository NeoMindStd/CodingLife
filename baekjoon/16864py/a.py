import sys;read=sys.stdin.readline
p,a,b=list(map(lambda n:round(float(n)*100),read().split()))
x=0
r=[]
while a*x<=p:
    y=(p-a*x)//b
    if a*x+b*y==p:r.append(f'{x} {y}')
    x+=1
print('\n'.join(r)if r else 'none')
