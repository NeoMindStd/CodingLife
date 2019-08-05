q = input()
q = q[:q.find('-')] + q[q.find('-'):].replace('+', '-')
l = q.split('-')
l[0] = l[0].split('+')
tmp = 0
for i in range(len(l[0])):
    tmp += int(l[0][i])
l[0] = tmp
for i in range(1, len(l)):
    l[0] -= int(l[i])
print(l[0])
