import re
n=int(input())
s=input()
r=''
for c in s:
    if c=='*':r+='.*';continue
    r+=c
p=re.compile(r)
for i in range(n):
    t=input()
    m=p.match(t)
    print('DA'if m is not None and m.group()==t else'NE')
