while True:
    n=int(input())
    if n == -1: break
    nums=[]
    for i in range(1, n):
        if n%i==0: nums.append(i)
    print(f'{n} = {" + ".join(map(str,nums))}' if sum(nums)==n else f'{n} is NOT perfect.')
