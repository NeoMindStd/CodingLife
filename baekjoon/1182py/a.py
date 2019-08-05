n, s = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

cnt = 0

def sumOfSubset(index, sos):
    if(index >= n):
        return

    global cnt
    sos += nums[index]
    cnt += 1 if sos == s else 0
    
    sumOfSubset(index+1, sos)
    sumOfSubset(index+1, sos-nums[index])

sumOfSubset(0, 0)
print(cnt)
