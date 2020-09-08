from collections import deque
from bisect import bisect

def solution(n, weak, dist):
    dist = dist[::-1]
    ld = len(dist)
    weak = tuple(weak)
    
    q = deque([(weak, 0)])
    enQ = q.append
    deQ = q.popleft
    visited = set()
    visited.add(weak)

    while q:
        wps, i = deQ()
        for j in range(len(wps)):
            idx = bisect(wps, (wps[j]+dist[i])%n)
            tmpWps = wps[:j]+wps[idx:] if j < idx else wps[idx:j]
            ni = i+1
            if not tmpWps: return ni
            if ni < ld and tmpWps not in visited:
                enQ((tmpWps, ni))
                visited.add(tmpWps)

    return -1
            
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
