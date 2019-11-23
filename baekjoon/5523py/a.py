import sys
read=sys.stdin.readline
s=[0,0]
for _ in range(int(read())):
    a,b=map(int,read().split())
    if a>b:s[0]+=1
    if a<b:s[1]+=1
print(*s)
