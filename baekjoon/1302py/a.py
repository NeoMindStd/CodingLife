import sys;read=sys.stdin.readline
d={}
for i in range(int(read())):
    s=input()
    try:d[s]+=1
    except:d[s]=1
d=d.items()
m=max(d,key=lambda x:x[1])[1]
print(sorted(filter(lambda x:x[1]==m,d),key=lambda x:x[0])[0][0])
