cards = [i for i in range(1, int(input())+1)]

cnt = 0
while len(cards) > 1:
    if cnt % 2 == 0:
        cards.pop(0)
    else:
        cards.append(cards.pop(0))
    cnt += 1

print(cards[0])
