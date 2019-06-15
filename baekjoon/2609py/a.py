a, b = input().split()
a = int(a)
b = int(b)

def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    else:
        return gcd(r, a)

def lcm(a,b) :
    return (a*b)//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))
