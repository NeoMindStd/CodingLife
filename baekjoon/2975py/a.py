while True:
    a,b,c=input().split()
    a,c=int(a),int(c)
    if a==c==0 and b=='W':break
    o='+'if b=='D'else'-'
    r=eval(f'{a}{o}{c}')
    if r<-200:print('Not allowed')
    else:print(r)
