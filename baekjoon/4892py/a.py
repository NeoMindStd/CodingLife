T=1
while True:
    a=int(input())*3
    if a==0:break
    f=a%2==0
    b=(a//2 if f else (a+1)//2)*3//9
    print(f'{T}. {"even"if f else"odd"} {b}')
    T+=1
