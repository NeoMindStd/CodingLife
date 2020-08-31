import math

n = int(input())
l = list(map(int,input().split()))
b, c = map(int,input().split())

print(sum(map(lambda x: 1 + math.ceil(max(0,x-b)/c), l)))
