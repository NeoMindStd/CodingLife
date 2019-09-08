street = []
    
n = int(input())
for i in range(n):
    street.append(tuple(map(int, input().split())))

values = [(street[0][0], street[0][1], street[0][2])]
for i in range(1, n):
    x = min(values[i-1][1],values[i-1][2]) + street[i][0]
    y = min(values[i-1][2],values[i-1][0]) + street[i][1]
    z = min(values[i-1][0],values[i-1][1]) + street[i][2]
    values.append((x, y, z))

print(min(values[n-1]))
