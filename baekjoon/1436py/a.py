n = int(input())

cnt = 0

i = 666
while True:
    if str(i).find("666") != -1:
        cnt += 1
    if cnt == n:
        print(i)
        break
    i += 1
