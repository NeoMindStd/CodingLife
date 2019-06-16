n = int(input())

fams = [[i for i in range(1,15)]]
for i in range(15):
    tmp = [1]
    for j in range(13):
        tmp.append(tmp[j]+fams[i][j+1])
    fams.append(tmp)

for i in range(n):
    a, b = int(input()), int(input())
    print(fams[a][b-1])
