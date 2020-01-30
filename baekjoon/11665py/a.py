import sys;read=sys.stdin.readline
l=[list(map(int,read().split()))for i in range(int(input()))]
p=[]
for i in range(3):p.append(max(l,key=lambda x:x[i])[i])
for i in range(3,6):p.append(min(l,key=lambda x:x[i])[i])
r=(p[3]-p[0])*(p[4]-p[1])*(p[5]-p[2])
print(r if r>0 else 0)
