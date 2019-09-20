x = int(input())

sticks = [64]

while sum(sticks) > x:
    sticks.sort(reverse=True)
    sticks[-1] //= 2
    if sum(sticks) >= x:
        continue
    sticks.append(sticks[-1])
print(len(sticks))
