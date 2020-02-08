import sys;read=sys.stdin.readline
def t(n):
    n=int(n)
    if n==1:return 2
    return 3 if n>0 else 4
while True:
    l=list(map(t,read()[:-1]))
    if l==[4]:break
    print(len(l)+1+sum(l))
