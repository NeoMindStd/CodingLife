import sys; read=sys.stdin.readline
for T in range(int(read())):
    p1=p2=0
    for _ in range(int(read())):
        c1,c2=read().split()
        if (c1=='R'and c2=='P')or\
           (c1=='P'and c2=='S')or\
           (c1=='S'and c2=='R'):
            p2+=1
        elif (c1=='R'and c2=='S')or\
             (c1=='P'and c2=='R')or\
             (c1=='S'and c2=='P'):
            p1+=1
        else:p1+=1;p2+=1
    if p1>p2:print("Player 1")
    elif p1<p2:print("Player 2")
    else :print("TIE")
