n = int(input())
comp = list(input())
for i in range(n-1):
    s = list(input())
    for j in range(len(comp)):
        if comp[j] == '?' or comp[j] != s[j]:
            comp[j] = '?'
print("".join(comp))
