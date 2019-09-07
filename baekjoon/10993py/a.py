n = int(input())

#1-1
#2-3, 5
#3-7, 13
#4-15, 29
#5-31, 61
#n-2**n-1, 2**(n+1)-3

row = 2**n-1
col = 2**(n+1)-3
triangle = [[' ']*(col) for _ in range(row)]

def draw_triangle(cnt, cur_row):
    if cnt % 2 != 0:
        pass
    else:
        pass
    draw_triangle(0, 0)

draw_triangle(0, 0)

result = ''
for i in range(len(triangle)):
    result += ''.join(map(str,triangle[i])) + '\n'

print(result)
