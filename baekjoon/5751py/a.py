while True:
    n=int(input())
    if n==0:break
    x=sum(map(int,input().split()))
    print(f'Mary won {n-x} times and John won {x} times')
