l=int(input())
s=[0]+list(sorted(map(int,input().split())))
n=int(input())
i=0
while s[i]<n:i+=1
a=(n-s[i-1])*(s[i]-n)-1
print(a if a>0 else 0)
