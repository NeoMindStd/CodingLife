for T in range(int(input())):
    a, b = map(int, input().split())
    a%=10
    al = [a]
    i = 0
    while True:
        n = ((al[i]%10)*a)%10
        if a == n:
            break
        al.append(n)
        i+=1

    r = al[(b-1)%len(al)]
    print(r if r != 0 else 10)
