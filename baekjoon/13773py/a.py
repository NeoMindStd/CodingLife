while True:
    n=int(input())
    if n==0:break
    if n%4!=0 or n<1896:r='No summer games'
    elif 1913<n<1919 or 1938<n<1946:r='Games cancelled'
    elif n>2020:r='No city yet chosen'
    else:r='Summer Olympics'
    print(n,r)
