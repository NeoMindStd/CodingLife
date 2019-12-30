a,b=map(int,input().split())
def c(a):
    a=a//2*2
    return (a*(a+1)//2-a*(a+1)//4-1)if a>3 else 0
print(c(b)-c(a-1))
