while True:
    n=list(input())
    if n[0]=='0':break
    f=True
    for i in range(len(n)//2):
        if n[i]!=n[-i-1]:
            f=False
            break
    print('yes'if f else'no')
