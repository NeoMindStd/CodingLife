while True:
    d,rh,rv=map(float,input().split())
    if d+rh+rv==0:break
    w=16/337**.5*d
    h=w*9/16
    print('Horizontal DPI: %.2f'%(rh/w))
    print('Vertical DPI: %.2f'%(rv/h))
