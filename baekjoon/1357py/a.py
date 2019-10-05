x, y = map(int, input().split())

def rev(n):
    n = list(str(n))
    n.reverse()
    return int("".join(map(str, n)))

print(rev(rev(x)+rev(y)))
