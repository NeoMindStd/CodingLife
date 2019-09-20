N = 10

# 1번의 경우
cnt = 0
for i in range(1, N+1): # N번 실행
    cnt+=1
cnt += 1 # 1번 실행
print("1번의 경우: ", cnt)

# 2번의 경우
cnt = 0
for i in range(1, N+1):
    for j in range(1, i+1): # for N 루프마다 i번 실행
        cnt += 1 
    cnt += 1 # for N 루프마다 1번 실행
print("2번의 경우: ", cnt)

# 3번의 경우
cnt = 0
for i in range(1, N+1):
    for j in range(1, i+1): # for N 루프마다 i번 실행
        for k in range(1, j+1): # for i 루프마다 j번 실행
            cnt += 1
        cnt += 1 # for i 루프마다 1번 실행
print("3번의 경우: ", cnt)

# 4번의 경우
cnt = 0
for i in range(1, N+1):
    for j in range(1, i+1): # for N 루프마다 i번 실행
        for k in range(1, j+1): # for i 루프마다 j번 실행
            cnt += 1
print("4번의 경우: ", cnt)
