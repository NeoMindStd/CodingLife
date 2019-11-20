n=int(input())
s=0
while n > 0:
    k=int(((1+8*n)**.5-1))//2
    s+=k
    n-=k*(k+1)//2
print(s)
