import sys;read=sys.stdin.readline
for T in range(3):
    s=sum([int(read())for _ in range(int(read()))])
    if s>0:print('+')
    elif s<0:print('-')
    else:print('0')
