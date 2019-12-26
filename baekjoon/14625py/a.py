a,b=map(int,input().split())
c,d=map(int,input().split())
n=input()
r=0
def q(l):
    try:
        l.index(n)
        return 1
    except: return 0
while a!=c or b!=d:
    r+=q('%02d%02d'%(a,b))
    b+=1
    if b>59:
        b%=60
        a+=1
r+=q('%02d%02d'%(a,b))
print(r)
