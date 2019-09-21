import sys
nums = [int(input()) for _ in range(int(sys.stdin.readline()))]

nums.sort()

d = [0]*8001
for n in nums:
    d[n+4000] += 1
tmp = max(d)
most = 4001
for i in range(-4000, 4001):
    if d[i+4000]==tmp:
        if most > i:
            most = i
        else:
            most = i
            break
ln = len(nums)
print(round(sum(nums)/ln))
print(nums[ln//2])
print(most)
print(abs(max(nums)-min(nums)))
