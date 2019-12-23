s=input().split()
def calc(a,b,c):
    a,c=int(a),int(c)
    if b=='+':return a+c
    elif b=='-':return a-c
    elif b=='*':return a*c
    else:
        if a>0<c:return a//c
        elif a<0:return -((-a)//c)
        elif c<0:return -(a//(-c))
        else:return (-a)//(-c)    
r=[calc(calc(s[0],s[1],s[2]),s[3],s[4]),calc(s[0],s[1],calc(s[2],s[3],s[4]))]
print(*sorted(r),sep='\n')
