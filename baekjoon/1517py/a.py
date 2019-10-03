import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def merge_sort(start, end):
    if start < end:
        mid = start + end
        mid //= 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)
        merge(start, mid, end)

wow = 0
def merge(start, mid, end):
    global wow
    cnt = 0
    first_i = start
    second_i = mid+1
    tmp = []
    while first_i <= mid or second_i <= end:
        if first_i <= mid and (second_i > end or\
                              nums[first_i] <= nums[second_i]):
            tmp.append(nums[first_i])
            first_i += 1
            wow += cnt
        else:
            tmp.append(nums[second_i])
            second_i += 1
            cnt += 1
    for i in range(end-start+1):
        nums[start+i] = tmp[i]

merge_sort(0, n-1)
print(wow)
    
    
