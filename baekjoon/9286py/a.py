import sys;read=sys.stdin.readline
r=''
for T in range(int(read())):
    r+=f'Case {T+1}:\n'
    for i in range(int(read())):
        n=int(read())
        if n<6:r+=f'{n+1}\n'
print(r)
