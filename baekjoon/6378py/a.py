while True:
    n=list(input())
    if n[0]=='0':break
    while len(n)>1:n=list(str(sum(map(int,n))))
    print(sum(map(int,n)))
