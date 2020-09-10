n = int(input())
paints = [{'X':set([]), '.':set([])} for _ in range(n)]

for no in range(n):
    for i in range(5):
        s = input()
        for j in range(len(s)):
            paints[no][s[j]].add((i, j))

diffs = []
for i in range(n):
    for j in range(i+1, n):
        diffs.append((abs(len(paints[i]['.'] - paints[j]['.'])) +\
                      abs(len(paints[i]['X'] - paints[j]['X'])),
                      i + 1, j + 1))

print(*list(min(diffs))[1:])
