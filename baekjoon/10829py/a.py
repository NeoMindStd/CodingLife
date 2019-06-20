n = int(input())

bi = list()
bi.append(n%2)

while n > 0:
    n//=2
    bi.append(n%2)

bi=list(map(str, bi))
print(int(''.join(bi)[::-1]))
