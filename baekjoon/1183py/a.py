n=int(input())
d={}
for i in range(n):
    s,a=map(int,input().split())
    try:d[s-a]+=1
    except:d[s-a]=1

print(d)
print(list(d.items()))
