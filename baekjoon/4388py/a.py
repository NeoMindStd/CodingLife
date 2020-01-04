while True:
    a,b=map(list,input().split())
    a=list(map(int,a))
    b=list(map(int,b))
    if a[0]==b[0]==0:break
    a.reverse()
    b.reverse()
    c=0
    for i in range(len(a), max(len(a),len(b))+1):a.append(0)
    for i in range(len(b), len(a)):b.append(0)
    for i in range(len(a)-1):
        if a[i]+b[i]>9:
            a[i+1]+=1
            c+=1
    print(c)
