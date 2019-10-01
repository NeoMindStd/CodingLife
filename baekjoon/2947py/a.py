woods = list(map(int, input().split()))

for i in range(len(woods)-1, 0, -1):
    for j in range(i):
        if woods[j] > woods[j+1]:
            woods[j], woods[j+1] = woods[j+1], woods[j]
            print(*woods)
