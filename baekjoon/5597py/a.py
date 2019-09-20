stu = dict()

for i in range(1, 31):
    stu[i] = False

for _ in range(28):
    stu[int(input())] = True

cnt = 0
for i in range(1, 31):
    if not stu[i]:
       cnt += 1
       print(i)
       if cnt >= 2:
           break
