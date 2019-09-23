datas = [int(input()) for _ in range(5)]
x = datas[0] * datas[4]
y = datas[1] + ((datas[3]*(datas[4]-datas[2])) if datas[2] < datas[4] else 0)
print(min(x, y))
