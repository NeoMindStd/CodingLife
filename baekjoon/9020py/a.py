# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

pri = prime_list(9974)

def bin_search(x, dest, start, end):
    index = (start + end) // 2
    if(x+pri[index] == dest):
        return index
    elif(start>=end):
        return -1
    elif(x+pri[index] < dest):
        start = index + 1
    else:
        end = index - 1
    return bin_search(x, dest, start, end)

for _ in range(int(input())):
    n = int(input())
    ans = 0, 10000
    for i in range(len(pri)):
        if(i > (n/2)): break
        j = bin_search(pri[i], n, i, len(pri)-1)
        if(j == -1): continue
        if(ans[1]-ans[0] > pri[j]-pri[i]): ans = pri[i], pri[j]
        if(ans[0]==ans[1]): break

    print(ans[0], ans[1])
