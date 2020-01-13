l=[0,1,2,3]
d={1:0,2:0,3:0}
for n in range(int(input())):
    a,b,g=map(int,input().split())
    l[a],l[b]=l[b],l[a]
    d[l[g]]+=1
print(max(d.values()))
