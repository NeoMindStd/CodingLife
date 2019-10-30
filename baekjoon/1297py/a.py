a,b,c=map(int,input().split())
x=(a*a/(b*b+c*c))**0.5
print(int(x*b), int(x*c))
