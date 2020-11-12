m = dict()
input()
for n in map(int, input().split()):
    try:m[n] += 1
    except: m[n] = 1

answer = list(sorted(filter(lambda t: t[0] == t[1], m.items()), key = lambda x:-x[0]))

if answer: print(answer[0][0])
elif 0 in m.keys(): print(-1)
else: print(0)
