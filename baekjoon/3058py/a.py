for T in range(int(input())):
    l=list(filter(lambda x:x%2==0,map(int,input().split())))
    print(sum(l),min(l))
