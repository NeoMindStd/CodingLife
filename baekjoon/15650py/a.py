n, m = map(int, input().split())

def backTracking(n, m, results, result):
    if len(result) >= m:
        results.append(result)
        return

    for i in range(result[-1] + 1, n-(m-len(result)) + 2):
        backTracking(n, m, results, result+[i])

results = []
for i in range(1, n-m+2):
    backTracking(n, m, results, [i])

for result in sorted(results): print(*result)
