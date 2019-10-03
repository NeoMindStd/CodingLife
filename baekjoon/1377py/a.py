import sys

n = int(sys.stdin.readline())
nums = [(0, -1)] + [(i, int(sys.stdin.readline())) for i in range(1, n+1)]

madmax = 0
nums.sort(key=lambda num: num[1])
for i in range(1, n+1):
    madmax = max(madmax, nums[i][0]-i)
print(madmax+1)
