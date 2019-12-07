t,r=0,[]
while True:
    t+=1
    a,b,c=map(int,input().split())
    if a==b==c==0:break
    r.append(f'Triangle #{t}\n')
    if a*a < c*c and b*b < c*c:
        if a < 0:r[-1]+=('a = %.3f' %(c*c-b*b)**.5)
        elif b < 0:r[-1]+=('b = %.3f' %(c*c-a*a)**.5)
        continue
    elif c < 0:
        r[-1]+=('c = %.3f' %(a*a+b*b)**.5)
        continue
    r[-1]+=('Impossible.')
print('\n\n'.join(r))
