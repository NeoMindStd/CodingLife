import sys;read=sys.stdin.readline
c=s=0
for i in sorted([list(map(int,read().split()))for _ in range(int(read()))],key=lambda x:(x[1],x[0])):
    if s<=i[0]:
        s=i[1]
        c+=1
print(c)
