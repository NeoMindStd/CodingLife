import sys;read=sys.stdin.readline
p,q,s=map(int,read().split())
def gcd(a,b):
    while b>0:a,b=b,a%b
    return a
print('no'if p*q//gcd(p,q)>s else'yes')
