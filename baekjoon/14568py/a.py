n,r=int(input()),0
t=2
while t <= n-4:
    y=1
    while t+y <= n-3:
        g=y+2
        while t+y+g <= n:
            if t+y+g==n: r+=1
            g+=1
        y+=1
    t+=2
print(r)
