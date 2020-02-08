import sys;read=sys.stdin.readline
l=list(map(int,read()[:-1]))
print('LUCKY'if sum(l[:len(l)//2])==sum(l[len(l)//2:]) else'READY')
