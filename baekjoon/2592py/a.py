s=0
d={}
for _ in range(10):
    n=int(input())
    try:d[n]+=1
    except:d[n]=1
    s+=n
print(s//10)
print(max(d.items(),key=lambda x:x[1])[0])
