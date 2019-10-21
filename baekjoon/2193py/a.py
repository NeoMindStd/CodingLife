pin = [1, 1]
n = int(input())
for i in range(2, n):
    pin.append(pin[i-1]+pin[i-2])
print(pin[n-1])
