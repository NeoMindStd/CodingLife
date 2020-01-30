v=int(input())
m=10**6*6
l=[]
for i in range(1,int(v**.5)+1):
    if v%i==0:
        l.append(i)
        if i*i!=v:l.append(v//i)
for a in l:
    for b in l:
        if v%(a*b)!=0:continue
        c=v//(a*b)
        m=min(m,(a*b+b*c+c*a)*2)
print(m)
