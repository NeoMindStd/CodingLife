n=int(input())
d={i+1:set([])for i in range(n)}
for i in range(1,int(n**.5)+1):
    for j in range(i+1):
        if i*i+j*j>n:continue
        for k in range(j+1):
            if i*i+j*j+k*k>n:continue
            for l in range(k+1):
                if i*i+j*j+k*k+l*l>n:continue
                if i*i+j*j+k*k+l*l==n:
                    t=tuple(filter(lambda x:x>0,[i,k,j,l]))
                    d[len(t)].add(t)
print(len(list(filter(lambda x:len(x)>0,d.values()))[0].pop()))
