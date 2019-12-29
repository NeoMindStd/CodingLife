import sys;read=sys.stdin.readline
n=int(read())
l=[int(read())for _ in range(n)]
l.sort(reverse=True)
m=0
while l:
    m=max(m,l[-1]*n)
    n-=1
    l.pop()
print(m)
