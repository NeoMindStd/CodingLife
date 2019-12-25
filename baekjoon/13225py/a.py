for T in range(int(input())):
    n=int(input())
    r=set()
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            r.add(i)
            r.add(n//i)
    print(n, len(r))
