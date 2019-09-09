n = int(input())

def prime_list(n):
    sieve = [True] * n
    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

pri = prime_list(n+1)
sp = set(pri)

sang = set()

for num in pri:
    if num in sang :
        continue
    tmp = set()
    tn = num
    cnt = 0
    while True:
        tmp.add(tn)
        tn = sum([int(i)**2 for i in list(str(tn))])
        if tn == 1:
            sang |= tmp & sp
            break
        if tn in tmp or cnt > 100:
            break
        cnt += 1
sang = list(sang)
sang.sort()
print("\n".join(map(str, sang)))
        
