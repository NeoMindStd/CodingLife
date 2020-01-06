import sys;read=sys.stdin.readline
n=int(read())
l=[0]+list(map(int,read().split()))
for i in range(n):l[i+1]+=l[i]
s=[]
for T in range(int(read())):
    i,j=map(int,read().split())
    s.append(l[j]-l[i-1])
print('\n'.join(map(str,s)))
