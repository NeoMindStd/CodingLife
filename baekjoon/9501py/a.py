for T in range(int(input())):
    n,d=map(int,input().split())
    l=[list(map(int,input().split()))for _ in range(n)]
    s=0
    for i in l:
       if d/i[0]*i[2]<=i[1]:s+=1
    print(s)
