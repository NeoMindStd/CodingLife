import sys

s = [sys.stdin.readline() for _ in range(5)]
result = ""
for j in range(15):
    for i in range(5):
        result += s[i][j] if j < len(s[i]) else ''
print("".join(map(str, result.split())))
