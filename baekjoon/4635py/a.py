while True:
    n=int(input())
    if n==-1:break
    l=[list(map(int,input().split()))for _ in range(n)]
    s=l[0][0]*l[0][1]
    for i in range(1,n):s+=l[i][0]*(l[i][1]-l[i-1][1])
    print(s,'miles')
