cnt = 0
for _ in range(int(input())):
    cnt += 1 if int(input()) != 0 else -1
print("Junhee is "+("not " if cnt < 0 else "") +"cute!")
