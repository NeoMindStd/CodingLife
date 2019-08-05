import math

m = int(input())
n = int(input())

minSqrt = math.ceil(math.sqrt(m))

if(minSqrt**2 > n):
    print(-1)
else:
    tmp = minSqrt
    s = 0
    while(tmp**2 <= n):
        s += tmp**2
        tmp += 1
    print(s)
    print(minSqrt**2)
