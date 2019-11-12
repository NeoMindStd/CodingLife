for T in range(int(input())):
    a,b,c=map(int,input().split())
    if b-a>c:print('advertise')
    elif b-a<c:print('do not advertise')
    else:print('does not matter')
