import sys;read=sys.stdin.readline
r=[]
for T in range(int(read())):
    s=0
    _,c=read(),int(read())
    for i in range(c):s+=int(read())
    r.append('YES'if s%c==0 else'NO')
print('\n'.join(r))
