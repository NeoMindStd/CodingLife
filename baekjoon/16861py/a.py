import sys;read=sys.stdin.readline
n=int(read())
while True:
    if n%sum(map(int,str(n)))==0:break
    n+=1
print(n)
