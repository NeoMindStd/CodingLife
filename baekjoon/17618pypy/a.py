r=0
for i in range(1,int(input())+1):
    s,t=0,i
    while t>0:
        s+=t%10
        t//=10
    if i%s==0:r+=1
print(r)
