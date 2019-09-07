n = int(input())

m = 2*n-1
triangle = [[' ']*(m) for _ in range(n)]

for i in range(n):
    for j in range(n-1-i, n+i):
        triangle[i][j] = ' '

def draw_space(cnt, end, row, col, pos):    
    if row == 0:
        triangle[row][col] = \
        triangle[row+1][col-1] = triangle[row+1][col+1] = \
        triangle[row+2][col-2] = triangle[row+2][col-2] = \
        triangle[row+2][col-1] = triangle[row+2][col-0] = \
        triangle[row+2][col+1] = triangle[row+2][col+2] = '*'
    else:
        if pos != "mid":
            for i in range(row, row+cnt):
                for j in range(col-i+row, col+i-row+1):
                    triangle[i][j] = triangle[i-cnt][j + (cnt if pos=="left" else -cnt)]
    
    if pos != "mid" or cnt * 2 > end:
        return
    draw_space(cnt, end, cnt, col-cnt, "left")
    draw_space(cnt, end, cnt, col+cnt, "right")
    draw_space(cnt*2, end, cnt*2, col, "mid")

draw_space(3, n, 0, m//2, "mid")

result = ''
for i in range(len(triangle)):
    result += ''.join(map(str,triangle[i])) + '\n'

print(result)
