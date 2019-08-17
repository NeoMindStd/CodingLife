n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = set()
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if(nums[i]+nums[j]+nums[k] <= m):
                sums.add(nums[i]+nums[j]+nums[k])

print(max(sums))
