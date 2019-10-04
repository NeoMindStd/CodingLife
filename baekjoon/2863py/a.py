a, b = map(int, input().split())
c, d = map(int, input().split())

nums = [c*d, d*b, b*a, a*c]
print(nums.index(min(nums)))
