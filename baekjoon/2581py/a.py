import math

m = int(input())
n = int(input())

exp = set()
primes = []
for i in range(2, n+1):
    if i in exp:
        continue
    flag = True
    for j in range(2,int(math.sqrt(i))+1):
        flag = j % 2 == 0
        if flag:
            break
    if flag and i >= m:
        primes.append(i)
    j = 1
    while i * j <= n:
        exp.add(i*j)
        j+=1

result = (str(sum(primes)) + "\n" + str(primes[0])) if primes else -1
print(result)
