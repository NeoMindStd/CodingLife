n,k,s=int(input()),int(input()),0
for i in range(k+1):
    s+=n
    n*=10
print(s)
