import sys;read=sys.stdin.readline
for T in range(int(read())):
    n=int(read())
    l=[max(list(map(int,read().split()))+[0]) for i in range(n)]
    print(sum(l))
