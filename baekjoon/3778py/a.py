import sys;read=sys.stdin.readline
s=[]
for T in range(int(read())):
    a,b=read(),read()
    c=dict()
    for ch in a:
        try:c[ch]+=1
        except:c[ch]=1
    for ch in b:
        try:c[ch]-=1
        except:c[ch]=-1
    r=0
    for k,v in c.items():r+=abs(v)
    s.append(f'Case #{T+1}: {r}')
print('\n'.join(s))
