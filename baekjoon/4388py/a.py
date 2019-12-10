while True:
    a,b=map(list,input().split())
    a=list(map(int,a))
    b=list(map(int,b))
    a.reverse()
    b.reverse()
    if a[0]==b[0]==0:break
    c=0
    for i in range(min(len(a), len(b))):
        if a[i]+b[i]>9:
            try:a[i+1]+=1
            except:pass
            c+=1
    print(c)
        
