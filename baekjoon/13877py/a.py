import sys;read=sys.stdin.readline
for T in range(int(read())):
    k,n=input().split()
    try:o=int(n,8)
    except:o=0
    print(k,o,int(n),int(n,16))
