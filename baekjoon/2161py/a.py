import collections

n = int(input())
cards = collections.deque([i for i in range(n, 0, -1)])

result = []
while True:
    result.append(cards.pop())
    if not cards:
        break
    cards.appendleft(cards.pop())

print(' '.join(map(str, result)))
