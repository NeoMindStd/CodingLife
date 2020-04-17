import sys
read=sys.stdin.readline
l1=list(map(int,read().split()))
l2=list(map(int,read().split()))
print(max(0,(min(l1[2],l2[2])-max(l1[0],l2[0])))*max(0,(min(l1[1],l2[1])-max(l1[3],l2[3]))))
