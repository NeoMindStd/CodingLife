for T in range(int(input())):print(max(list(map(lambda x: (int(x[1]),x[0]),[input().split() for _ in range(int(input()))])))[1])
