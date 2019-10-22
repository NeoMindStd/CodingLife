n, f, rj = int(input()), int(input()), []
nums = [[0]*n for _ in range(n)]
i, j, v = -1, 0, n*n
while v > 0:
    while i+1 < n and nums[i+1][j] == 0:
        i+=1
        nums[i][j], rj = v, [i+1, j+1] if v==f else rj
        v-=1
    while j+1 < n and nums[i][j+1] == 0:
        j+=1
        nums[i][j], rj = v, [i+1, j+1] if v==f else rj
        v-=1
    while i-1 < n and nums[i-1][j] == 0:
        i-=1
        nums[i][j], rj = v, [i+1, j+1] if v==f else rj
        v-=1
    while j-1 < n and nums[i][j-1] == 0:
        j-=1
        nums[i][j], rj = v, [i+1, j+1] if v==f else rj
        v-=1
result = ""
for row in nums:
    result+=" ".join(map(str, row))+"\n"
print(result[:-1])
print(*rj)
