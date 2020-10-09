from collections import deque

n, w, L = map(int, input().split())
a = list(map(int, input().split()))[::-1]
b = []
bridge = deque([0]*w)

t = 0
while a or sum(bridge) > 0:
    b.append(bridge.popleft())

    if a and sum(bridge) + a[-1] <= L: bridge.append(a.pop())
    else: bridge.append(0)
    
    t += 1

print(t)
