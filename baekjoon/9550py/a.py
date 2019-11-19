for T in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    print(sum(map(lambda x:x//k,l)))
