n = int(input())
paper = []
blue = 0
white = 0

for _ in range(n):
    paper.append(list(map(int, input().split())))

def cut(x, y, length):
    global paper, blue, white
    
    if length == 1:
        if paper[x][y] == 1:
            blue += 1
        else :
            white += 1
        return
    
    flag = False
    i = x
    while i < x + length:
        j = y
        while j < y + length:
            flag = paper[x][y] != paper[i][j]
            if flag:
                break
            j += 1
        if flag:
            break
        i += 1

    if flag:
        tmp = length // 2
        cut(x, y, tmp)
        cut(x, y + tmp, tmp)
        cut(x + tmp, y, tmp)
        cut(x + tmp, y + tmp, tmp)
    else:
        if paper[x][y] == 1:
            blue += 1
        else :
            white += 1
        return

cut(0, 0, n);
print(white)
print(blue)
