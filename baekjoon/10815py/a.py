import sys

n = int(sys.stdin.readline())
cards = set(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    nums[i] = 1 if nums[i] in cards else 0
print(' '.join(map(str,nums)))
