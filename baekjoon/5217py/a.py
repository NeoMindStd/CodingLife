for T in range(int(input())):
    n,l=int(input()),[]
    for i in range(1,n//2+1):
        if 1<=n-i<=12 and i!=n-i:l.append(f'{i} {n-i}')
    print(f'Pairs for {n}:',', '.join(l))
