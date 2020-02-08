import sys
for T in sys.stdin:
    d,f,g=map(int,T.split())
    print('N'if 12/f<(144+d*d)**.5/g else'S')
