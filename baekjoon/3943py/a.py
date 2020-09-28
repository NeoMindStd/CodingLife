import sys; read = sys.stdin.readline

result = []
for T in range(int(read())):
    n = int(read())
    nums = [n]
    
    while nums[-1] > 1:
        if nums[-1] % 2 > 0: nums.append(nums[-1] * 3 + 1)
        else: nums.append(nums[-1] // 2)

    result.append(max(nums))

print('\n'.join(map(str, result)))
