nums = [int(input()) for _ in range(7)]
nums = list(filter(lambda num: num%2==1, nums))
if not nums:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
