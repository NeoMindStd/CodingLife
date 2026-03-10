import sys
from collections import deque

read = sys.stdin.readline

t = int(read())
answers = []

for _ in range(t):
    n, k = map(int, read().split())
    build_time = [0] + list(map(int, read().split()))

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, read().split())
        graph[x].append(y)
        indegree[y] += 1

    target = int(read())

    dp = [0] * (n + 1)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dp[i] = build_time[i]
            q.append(i)

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            cand = dp[cur] + build_time[nxt]
            if dp[nxt] < cand:
                dp[nxt] = cand

            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    answers.append(str(dp[target]))

print("\n".join(answers))
