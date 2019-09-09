n, k = map(int, input().split())

def eratos(n, k):
    n += 1
    sieve = [True] * n
    tmp = 0
    
    for i in range(2, n):
        if sieve[i] == True:
            for j in range(i, n, i):
                if sieve[j]:
                    tmp += 1
                    sieve[j] = False
                    if tmp == k:
                        print(j)
                        return

eratos(n, k)
