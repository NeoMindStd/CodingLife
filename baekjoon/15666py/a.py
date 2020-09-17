n, m = map(int, input().split())
numbers = list(sorted(map(int, input().split())))

def backTracking(n, m, results, result):
    if len(result) >= m:
        results.add(tuple(map(lambda i:numbers[i], result)))
        return

    for i in range(result[-1], n):
        backTracking(n, m, results, result+[i])

results = set()
for i in range(n): backTracking(n, m, results, [i])

for result in sorted(results): print(*result)
