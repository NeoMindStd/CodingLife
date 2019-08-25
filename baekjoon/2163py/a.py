n, m = map(int, input().split())

def crack(n, m):
    if n == m == 1:
        return 0
    else:
        if n >= m:
            return 1 + crack(n//2, m) + crack(n-n//2, m)
        else:
            return 1 + crack(n, m//2) + crack(n, m-m//2)

print(crack(n, m))
