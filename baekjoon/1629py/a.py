a, b, c = map(int, input().split())

def power(a, b, c):
    if b==1:
        return a%c
    elif b%2==0:
        tmp = power(a, b//2, c)
        return (tmp%c*tmp)%c
    else:
        tmp = power(a, (b-1)//2, c)
        return ((tmp%c*tmp)%c*a)%c
print(power(a%c,b,c))
 
