T=1
while True:
    o,w=map(int,input().split())
    if o==w==0:break
    while True:
        a,n=input().split()
        n=int(n)
        if a=='#':break
        elif w>0 and a=='F':w+=n
        else: w-=n
    if w<=0:print(T,'RIP')
    elif o/2<w<o*2:print(T,':-)')
    else: print(T,':-(')
    T+=1
