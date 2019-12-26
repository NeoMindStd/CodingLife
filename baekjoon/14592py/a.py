l=[list(map(int,input().split()))+[i+1]for i in range(int(input()))]
t=[]
m=max(l,key=lambda x:x[0])[0]
for i in l:
    if i[0]==m:t.append(i)
l=[]
m=min(t,key=lambda x:x[1])[1]
for i in t:
    if i[1]==m:l.append(i)
print(min(l,key=lambda x:x[2])[3])
