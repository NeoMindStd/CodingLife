n = int(input())

fibo = [2, 1, 1]

while fibo[0] < n:
    fibo.append(fibo[-1]+fibo[-2])
    fibo[0]+=1

print(fibo[n])
