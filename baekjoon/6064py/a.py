def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r    
    return x

def lcm(x, y):
    return x*y//gcd(x,y)

for i in range(int(input())):
    M, N, x, y = tuple(map(int, input().split()))

    xx = yy = k = 0
    end = lcm(M, N)
    flag = True
    while True:
        k += 1
        tmp = (xx+1) % (M+1)
        xx = tmp if tmp != 0 else 1
        tmp = (yy+1) % (N+1)
        yy = tmp if tmp != 0 else 1
        if (x, y) == (xx, yy):
            break
        if k >= end:
            flag = False
            break
    print(k if flag else -1)
 
