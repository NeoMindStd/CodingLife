import sys

for a in sys.stdin:
    print('Y' if int(a)%6 == 0 else 'N')
