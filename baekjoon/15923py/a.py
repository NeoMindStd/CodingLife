r=int(input())
l=[list(map(int,input().split()))for i in range(r)]
s=0
for i in range(r):s+=int(((l[i][0]-l[(i+1)%r][0])**2+(l[i][1]-l[(i+1)%r][1])**2)**.5)
print(s)
