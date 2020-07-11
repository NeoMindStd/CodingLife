a,b,k=map(int,input().split())
print((a//k)*(b//k)-max(0,a//k-2)*max(0,b//k-2))
