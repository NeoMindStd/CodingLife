n=int(input())
l=[[0]*7 for _ in range(n)]
p=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for v in p[i]:l[i][v] += 1
    t=[]
    for j in range(1,7):
        if max(l[i])==l[i][j]:t.append(j)
    if len(t)>2: l[i][0]=max(t)*100
    elif len(t)>1: l[i][0]=2000+t[0]*500+t[1]*500
    else: 
        if l[i][t[0]] == 2: l[i][0]=1000+t[0]*100
        elif l[i][t[0]] == 3: l[i][0]=10000+t[0]*1000
        else: l[i][0]=50000+t[0]*5000
    
print(max(l, key=lambda x: x[0])[0])
