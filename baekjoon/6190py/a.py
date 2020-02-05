import sys;read=sys.stdin.readline
n,s=int(input()),0
while True:
    if n==1:break
    if n%2==0:n//=2
    else:n=n*3+1
    s+=1
print(s)
