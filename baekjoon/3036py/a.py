def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    
    return a

input()
rings = list(map(int, input().split()))

for i in range(1, len(rings)):
    g = gcd(rings[0], rings[i])
    print("%d/%d" %(rings[0]//g, rings[i]//g))
