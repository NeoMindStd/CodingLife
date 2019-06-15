count = int(input())

a = int(input())

aSum=0

for i in range(count):
    aSum += a % 10
    a //= 10

print(aSum)
