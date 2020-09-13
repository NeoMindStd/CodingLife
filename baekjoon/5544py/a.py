n = int(input())
dic = {i:0 for i in range(1, n+1)}

for _ in range(n*(n-1)//2):
    a, b, c, d = map(int, input().split())
    if c > d: dic[a] += 3
    elif c < d: dic[b] += 3
    else:
        dic[a] += 1
        dic[b] += 1

scores = list(sorted(dic.values(), reverse=True))

for score in dic.values():
    print(scores.index(score) + 1)
