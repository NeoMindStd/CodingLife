for T in range(int(input())):
    n,m=map(int,input().split())
    print(f'Scenario #{T+1}:\n{(m*(m+1)-n*(n+1))//2+n}\n')
