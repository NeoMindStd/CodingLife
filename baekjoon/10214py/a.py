for T in range(int(input())):
    a=b=0
    for _ in range(9):
        c,d=map(int,input().split())
        a+=c
        b+=d
    if a>b:print('Yonsei')
    elif a<b:print('Korea')
    else: print('Draw')
