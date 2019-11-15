a=b=100
for r in range(int(input())):
    c,d=map(int,input().split())
    if c<d:a-=d
    elif c>d:b-=c
print(f'{a}\n{b}')
