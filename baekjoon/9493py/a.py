while True:
    a,b,c=map(int,input().split())
    if b<1:break
    t=a*3600/b-a*3600/c
    h=t//3600
    t%=3600
    m=t//60
    print('%d:%02d:%02d'%(h,m,round(t%60)))
