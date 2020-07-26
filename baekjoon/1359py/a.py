n,m,k=map(int,input().split())
def fact(n): return  1 if n<2 else fact(n-1)*n
def comb(n,r): return fact(n)/(fact(n-r)*fact(r))
print(comb(m,k)/comb(n,m))
