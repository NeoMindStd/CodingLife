n=int(input())
l,m=[],100000000
i=1
while i**3<=n:
    j=i
    while i*j*j<=n:
        k=n//i//j
        if i*j*k!=n:j+=1;continue
        a=i*j+j*k+k*i
        if a<m:
            m=a
            l=[i,j,k]
        j+=1
    i+=1
print(*l)
