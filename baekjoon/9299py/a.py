import sys;read=sys.stdin.readline
for T in range(int(read())):
    l=list(map(int,input().split()))
    for i in range(1,l[0]+1):
        l[i]*=l[0]-i+1
    print(f'Case {T+1}: {l[0]-1}',*l[1:-1])
