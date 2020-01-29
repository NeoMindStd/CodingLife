while True:
    n=int(input())
    if n==-1:break
    l=[list(map(int,input().split()))for _ in range(n)]
    h=l[0][1]
    d=l[0][0]*h
    for i in range(1,n):d,h=d+l[i][0]*(l[i][1]-h),l[i][1]
    print(d,'miles')
