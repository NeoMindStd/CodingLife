a,b,c=map(int,input().split())
l={}
for i in range(a):
    for j in range(b):
        for k in range(c):
            s=i+j+k+3
            try:l[s]+=1
            except:l[s]=1
print(max(l.items(), key=lambda x:x[1])[0])
