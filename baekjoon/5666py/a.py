while True:
    try:a,b=map(int,input().split())
    except EOFError:break
    print('%.2f'%(a/b))
