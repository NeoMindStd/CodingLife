n, m = int(input()), int(input())

a = min(m + 60, n)
b = n - a
print(a * 1500 + b * 3000)
