n = 1000-int(input())

cnt = n // 500
n%=500
cnt += n // 100
n%=100
cnt += n // 50
n%=50
cnt += n // 10
n%=10
cnt += n // 5
n%=5
cnt += n // 1
n%=1


print(cnt)
