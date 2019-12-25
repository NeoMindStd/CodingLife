a,b,c,d=input().split()
if a==b and (\
    a=='S' and (c=='R'or d=='R')or\
    a=='R' and (c=='P'or d=='P')or\
    a=='P' and (c=='S'or d=='S')):print('TK')
elif c==d and (\
    c=='S' and (a=='R'or b=='R')or\
    c=='R' and (a=='P'or b=='P')or\
    c=='P' and (a=='S'or b=='S')):print('MS')
else:print('?')
