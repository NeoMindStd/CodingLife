while(True):
    nums = list(map(int, input().split()))
    n = nums[0]
    if(n == 0):
        break
    nums = nums[1:]
    for i1 in range(n-5):
        for i2 in range(i1+1, n-4):
            for i3 in range(i2+1, n-3):
                for i4 in range(i3+1, n-2):
                    for i5 in range(i4+1, n-1):
                        for i6 in range(i5+1, n):
                            print(nums[i1],nums[i2],nums[i3],nums[i4],nums[i5],nums[i6])
    print()
