n,c=map(int,input().split())
l,r=[list(map(int,input().split(':')))for _ in range(n)],-c*(n-1)
for i in l:r+=i[0]*60+i[1]
print('%02d:%02d:%02d'%(r//3600,r%3600//60,r%60))
