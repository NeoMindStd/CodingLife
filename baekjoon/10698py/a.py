for T in range(int(input())):
    a,b=input().split('=')
    c=eval(a+'=='+b)
    print(f'Case {T+1}: {"YES"if c else"NO"}')
