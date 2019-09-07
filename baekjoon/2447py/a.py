n = int(input())

triangle = [['*']*(n) for _ in range(n)]

for step in range(n):
    for x_pos in range(3**step, n, 3**(step+1)):
        for y_pos in range(3**step, n, 3**(step+1)):
            for i in range(3**step):
                for j in range(3**step):
                    triangle[x_pos+i][y_pos+j] = ' '

result = ''
for i in range(len(triangle)):
    result += ''.join(map(str,triangle[i])) + '\n'

print(result)
