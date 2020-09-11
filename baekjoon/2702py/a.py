def gcd(a, b):
    while b > 0: a, b = b, a % b
    return a

for T in range(int(input())):
    a, b = map(int, input().split())
    g = gcd(a,b)
    print(a * b // g, g)
