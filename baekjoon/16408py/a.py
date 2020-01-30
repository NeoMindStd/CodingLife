l=input().split()
d={}
for i in l:
    try:d[i[0]]+=1
    except:d[i[0]]=1
print(max(d.values()))
