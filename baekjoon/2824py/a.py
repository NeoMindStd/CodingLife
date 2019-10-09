n = int(input())
a = eval("*".join(map(str, input().split())))
m = int(input())
b = eval("*".join(map(str, input().split())))

def gcd(m,n):
    while n != 0:
       t = m%n
       m, n = n, t
    return m

val = gcd(a, b)
print(("%09d" %(val%1000000000)) if val > 999999999 else val)
