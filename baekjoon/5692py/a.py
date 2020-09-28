import sys; read = sys.stdin.readline

factorial = [1]
for i in range(5): factorial.append(factorial[i] * (i + 1))

result = []
while True:
    n = read()[:-1]
    if int(n) == 0: break

    acc = 0
    for i in range(1, len(n) + 1):
        acc += int(n[len(n) - i]) * factorial[i]

    result.append(acc)

print('\n'.join(map(str, result)))
