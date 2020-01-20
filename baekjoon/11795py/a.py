A=B=C=0
for T in range(int(input())):
    a,b,c=map(int,input().split())
    A+=a
    B+=b
    C+=c
    m=min(A,B,C)
    if m<30:print('NO')
    else:
        A-=m
        B-=m
        C-=m
        print(m)
