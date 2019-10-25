n = int(input())

#1-1
#2-3, 5
#3-7, 13
#4-15, 29
#5-31, 61
#n-2**n-1, 2**(n+1)-3

shapes = []
for idx in range(1, n+1):
    tri = [[' ']*(2**(idx+1)-3) for _ in range(2**idx-1)]
    if idx % 2 != 0:
        for i in range(2**idx-2):
            tri[i][2**idx-2-i]='*'
            tri[i][2**idx-2+i]='*'
        tri[2**idx-2]=['*']*(2**(idx+1)-3)
        for i in range(2**(idx-1)-1, 2**idx-2):
            for j in range(2**(idx-1), 3*(2**(idx-1))-3):
                tri[i][j] = shapes[-1][i-(2**(idx-1)-1)][j-(2**(idx-1))]
    else:
        tri[0]=['*']*(2**(idx+1)-3)
        for i in range(1, 2**idx-1):
            tri[i][i]='*'
            tri[i][2**(idx+1)-4-i]='*'
        for i in range(1, 2**(idx-1)):
            for j in range(2**(idx-1), 3*(2**(idx-1))-3):
                tri[i][j] = shapes[-1][i-1][j-(2**(idx-1))]
    shapes.append(tri)

r = ''
for row in shapes[-1]:
    for i in range(len(row)-1, -1, -1):
        if row[i] == '*':
            tmp = row[0:i+1]
            break
    r += "".join(map(str, tmp))+"\n"
print(r)
