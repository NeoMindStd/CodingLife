import math

for x in range(int(input())):
    a, b = input().split()
    n = int(b)-int(a)
    
    ms = int(math.sqrt(n))

    d = n-ms
    for i in range(1, ms):
        d -= i*2

    rd = 0
    try:
        rd = d//ms + (1 if d%ms>0 else 0)
    except ZeroDivisionError:
        rd = d
    print(2*ms-1+rd)
