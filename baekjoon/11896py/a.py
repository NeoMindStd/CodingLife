a,b=map(int,input().split())
a,b=max((a+1)//2-1,1),max(b//2,1)
print(b*(b+1)-a*(a+1))
