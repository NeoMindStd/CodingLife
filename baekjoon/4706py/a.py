while True:
    ta,tb=map(float,input().split())
    if ta==tb==0:break
    print('%.3f'%((1-tb*tb/(ta*ta))**.5))
