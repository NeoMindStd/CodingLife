import math
input()
l=map(int,input().split())
s=int(input())
ea=0
for file in l: ea+=math.ceil(file/s)
print(ea*s)
