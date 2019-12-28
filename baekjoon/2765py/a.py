t=1
while True:
    a,b,c=map(float,input().split())
    if b==0:break
    d=a/63360*3.141592*b
    print('Trip #%d: %.2f %.2f'%(t,d,d*3600/c))
    t+=1
