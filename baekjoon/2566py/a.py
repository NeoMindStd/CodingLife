l=[list(map(int,input().split())) for _ in range(9)]
for i in range(9):
    l[i].append(max(l[i]))
t=l.index(max(l, key=lambda x:x[-1]))
print(l[t][-1])
print(t+1,l[t].index(max(l[t][0:9]))+1)
