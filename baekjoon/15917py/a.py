import sys;read=sys.stdin.readline
r=[]
for T in range(int(read())):
    q=int(read())
    r.append('1'if q&-q==q else'0')
print('\n'.join(r))
