import sys

def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r    
    return x

def lcm(x, y):
    return x*y//gcd(x,y)

for i in range(int(sys.stdin.readline())):
    M, N, x, y = tuple(map(int, sys.stdin.readline().split()))

    end = lcm(M, N)
    
    if True if M > N else (False if M < N else x > y):
        years = [x + M*i for i in range((end-x)//M+1)]
    else:
        years = [y + N*i for i in range((end-y)//N+1)]

    flag = False
    for year in years:
        if (year%M, year%N) == (x%M, y%N):
            flag = True
            break
    print(year if flag else -1)
