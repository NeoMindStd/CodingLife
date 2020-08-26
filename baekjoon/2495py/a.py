for T in range(3):
    t,a,p='',0,1
    for c in input():
        if t==c: p+=1
        else: p=1
        a=max(a,p)
        t=c
    print(a)
