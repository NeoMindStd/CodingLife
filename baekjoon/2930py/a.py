r = int(input())
s = input()
n = int(input())
fs = [input() for _ in range(n)]

rsp = {'R':0,'S':1,'P':2}

cs = ms = 0
for i in range(r):
    ts = [[0,'R'],[0,'S'],[0,'P']]
    for j in range(n):
        if (rsp[s[i]] + 1) % 3 == rsp[fs[j][i]]: cs += 2
        elif s[i] == fs[j][i]: cs += 1

        for t in ts:
            if (rsp[t[1]] + 1) % 3 == rsp[fs[j][i]]: t[0] += 2
            elif t[1] == fs[j][i]: t[0] += 1
    ms += max(ts)[0]
print(cs)
print(ms)
