n=int(input())
r=0
for i in range(min(100,n)):
    if n-i<100:r+=1
print(r)
