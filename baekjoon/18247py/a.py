for T in range(int(input())):
    a,b=map(int, input().split())
    if b<4 or a<12:n=-1
    else:n=11*b+4
    print(n)
