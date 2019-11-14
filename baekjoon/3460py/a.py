for T in range(int(input())):
    n,r,i=int(input()),[],0
    while n>0:
        if n % 2 == 1:
            r.append(i)
        n//=2
        i+=1
    print(*r)
