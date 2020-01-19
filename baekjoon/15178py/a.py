for T in range(int(input())):
    a,b,c=map(int,input().split())
    print(a,b,c,'Check'if a+b+c!=180 else'Seems OK')
