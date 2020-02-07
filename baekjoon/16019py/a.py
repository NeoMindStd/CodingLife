import sys;read=sys.stdin.readline
l=list(map(int,read().split()))
for i in range(5):
    r=[0]*5
    for j in range(i+1,5):r[j]=r[j-1]+l[j-1]
    for j in range(i-1,-1,-1):r[j]=r[j+1]+l[j]
    print(*r)
