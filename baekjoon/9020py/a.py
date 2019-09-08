from sys import stdin

def prime_list(n):
    sieve = [True] * n
    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

pri = prime_list(50000)

def bin_search(x, dest, start, end):
    while True:
        index = (start + end) // 2
        if(x+pri[index] == dest):
            return index
        elif(start>=end):
            return -1
        elif(x+pri[index] < dest):
            start = index + 1
        else:
            end = index - 1

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ans = 0, 10000
    for i in range(len(pri)):
        if(i > (n/2)): break
        j = bin_search(pri[i], n, i, len(pri)-1)
        if(j == -1): continue
        if(ans[1]-ans[0] > pri[j]-pri[i]): ans = pri[i], pri[j]
        if(ans[0]==ans[1]): break

    print(" ".join(map(str, ans)))
