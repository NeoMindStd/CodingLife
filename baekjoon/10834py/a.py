import sys;read=sys.stdin.readline
l=[list(map(int,read().split()))for i in range(int(read()))]
r=1
for s in l:r=int(r*s[1]/s[0]*(-s[2]*2+1))
print(1 if r<0 else 0,abs(r))
