import sys
a = int(sys.stdin.readline())
op = sys.stdin.readline()
b = int(sys.stdin.readline())
print(a*b if op[0]=='*' else a+b)
