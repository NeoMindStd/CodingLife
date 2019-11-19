for T in range(int(input())):
    n=int(input())
    l=[25,10,5,1]
    r=[]
    for i in l:
        r.append(n//i)
        n%=i
    print(*r)
