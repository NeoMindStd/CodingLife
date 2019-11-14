l=sorted(list(map(int,input().split())))
n=l[1]-l[0]+1
print(n*l[0]+n*(n-1)//2)
