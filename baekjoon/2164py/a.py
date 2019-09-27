import collections

n = int(input())
cards = collections.deque([i for i in range(n, 0, -1)])

while True:
    tmp = cards.pop()
    if not cards:
        print(tmp)
        break
    cards.appendleft(cards.pop())
