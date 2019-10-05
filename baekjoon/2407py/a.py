n, m = map(int, input().split())
def fact(n):
    if n < 2:
        return 1
    else:
        return n*fact(n-1)
print(fact(n)//(fact(n-m)*fact(m)))
