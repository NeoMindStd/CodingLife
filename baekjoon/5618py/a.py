input()
l=list(map(int,input().split()))

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

t=gcd(gcd(l[0],l[1]),gcd(l[1],l[-1]))
r=[]
for i in range(1,int(t**0.5)+1):
    if t%i==0: r.append(i)
s=len(r)
for i in range(1,s+1):
    p=t//r[s-i]
    if p*p!=t:r.append(p)
print('\n'.join(map(str,r)))
