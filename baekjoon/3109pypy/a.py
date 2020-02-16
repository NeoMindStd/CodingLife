import sys;read=sys.stdin.readline
r,c=map(int,read().split())
l=[list(read().strip())for _ in range(r)]
d=(-1,0,1)
stack,a=[],0

for i in range(r):
    ci=i
    cj=j=c-1
    while True:
        if cj<1:
            while stack:
                l[ci][cj]='o'
                ci,cj=stack.pop()
            l[ci][cj]='o'
            a+=1
            break
        f=False
        for k in range(3):
            if 0<=ci+d[k]<r and l[ci+d[k]][cj-1]=='.':
                f=True
                stack.append((ci,cj))
                ci,cj=ci+d[k],cj-1
                break
        if not f:
            l[ci][cj]='_'
            try:ci,cj=stack.pop()
            except:break
            
print(a)
