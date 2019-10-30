while True:
    s1,s2=input(),input()
    p1=p2=0
    for i in range(len(s1)):
        a,b=s1[i],s2[i]
        if (a=='R' and b=='S') or\
           (a=='S' and b=='P') or\
           (a=='P' and b=='R'):
            p1+=1
        elif (b=='R' and a=='S') or\
             (b=='S' and a=='P') or\
             (b=='P' and a=='R'):
            p2+=1
    if s1 == 'E':
        break
    print(f'P1: {p1}\nP2: {p2}')
