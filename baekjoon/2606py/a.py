n = int(input())
coms = []
for _ in range(int(input())):
    coms.append(tuple(map(int, input().split())))
infected = {1}

i = 0
flag = False
while True:
    if len(coms) == 0 or i + 1 == len(coms) and not flag: break
        
    if coms[i][0] in infected:
        infected.add(coms[i][1])
        coms.pop(i)
        flag = True
    elif coms[i][1] in infected:
        infected.add(coms[i][0])
        coms.pop(i)
        flag = True
    else: i += 1

    if i == len(coms) and flag:
        i = 0
        flag = False
        
print(len(infected)-1)
