n, m = map(int, input().split())
numbers = list(map(int, input().split()))

def backTracking(n, m, results, result):
    if len(result) >= m:
        results.append(list(map(lambda i:numbers[i], result)))
        return

    for i in range(n):
        if i in result:continue
        backTracking(n, m, results, result+[i])

results = []
for i in range(n): backTracking(n, m, results, [i])

for result in sorted(results): print(*result)
