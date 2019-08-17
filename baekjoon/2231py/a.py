n = int(input())

for x in range(1, n):
    if x + sum(list(map(int, list(str(x))))) == n:
        print(x)
        break
    elif x == n-1:
        print(0)
        break
if n == 1:
    print(0)
