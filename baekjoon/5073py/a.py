while True:
    l=sorted(map(int,input().split()))
    if l[2]==0:break
    if l[0]==l[2]:print('Equilateral')
    elif l[0]+l[1]<=l[2]:print('Invalid')
    elif l[0]==l[1]or l[1]==l[2]:print('Isosceles')
    else:print('Scalene')
