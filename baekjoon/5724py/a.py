while True:
    n,s=int(input()),0
    if n==0:break
    for i in range(n,0,-1):s+=i*i
    print(s)
