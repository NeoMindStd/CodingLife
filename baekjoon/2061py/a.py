a,b=map(int,input().split())
r=''
for i in range(2, min(int(a**.5)+1,b+1)):
    if a%i==0:
        r='GOOD'if i>=b else f'BAD {i}'
        break
if r=='':r='GOOD'
print(r)
