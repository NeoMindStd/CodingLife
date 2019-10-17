print(sum(list(map(lambda t: t[1]%t[0], [tuple(map(int, input().split())) for _ in range(int(input()))]))))
