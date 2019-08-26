n = int(input())

fibo = [0, 1]
while len(fibo) <= n:
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[-1])
