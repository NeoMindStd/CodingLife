date = int(input())
cars = list(map(int, input().split()))
cnt = 0
for car in cars:
    cnt += 1 if car % 10 == date % 10 else 0
print(cnt)
