import sys;read=sys.stdin.readline

n=int(read())
a,l=[0,0,0],[list(map(int,read().split()))for _ in range(n)]

def div(si,ei,sj,ej):
    global a,l
    f=False
    for i in range(si,ei):
        for j in range(sj,ej):
            if l[i][j]!=l[si][sj]:
                f=True
                break
        if f:break
    if f:
        for i in range(3):
            for j in range(3):
                ti,tj=si+(ei-si)//3*i,sj+(ej-sj)//3*j
                div(ti,ti+(ei-si)//3,tj,tj+(ej-sj)//3)
    else:a[l[si][sj]+1]+=1

div(0,n,0,n)
print(*a,sep='\n')
