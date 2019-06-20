_, towers = input(), list(map(int, input().split()))

for i, tower in enumerate(towers):
    dst = 0
    for j in range(i-1, -1, -1):
        if(tower <= towers[j]):
            dst = j+1
            break
    print(dst, end=" ")
