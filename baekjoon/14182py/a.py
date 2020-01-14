while True:
    n=int(input())
    if n==0:break
    if 5000000>=n>1000000:n*=0.9
    if 5000000<n:n*=0.8
    print(int(n))
