numbers = list(range(1, 10001))

for i in range(1, 10000):
    value = i + i %10
    while(i//10 > 0):
        i //= 10
        value += i %10
    try:
        numbers.remove(value)
    except ValueError:
        continue
    

for self_number in numbers:
    print(self_number)
