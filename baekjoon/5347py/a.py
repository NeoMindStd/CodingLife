import sys;read=sys.stdin.readline
def gcd(a,b):
    while b>0:a,b=b,a%b
    return a
for T in range(int(read())):
    a,b=map(int,read().split())
    print(a*b//gcd(a,b))
