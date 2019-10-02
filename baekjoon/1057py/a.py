n, k, l = map(int, input().split())
people = [i for i in range(1, n+1)]

cnt = 1
flag = False
while True:
    for i in range(n//2):
        first = people[2*i]
        second = people[2*i+1]
        if (k, l) == (first, second) or\
        (l, k) == (first, second):
            print(cnt)
            flag = True
            break
        elif k == first or k == second:
            people[i] = k
        elif l == first or l == second:
            people[i] = l
        else:
            people[i] = first
    if flag or n==1:
        break
    if n % 2 == 1:
        people[i+1] = people[n-1]
    n  = n // 2 + n % 2
    cnt += 1
if not flag:
    print(-1)
