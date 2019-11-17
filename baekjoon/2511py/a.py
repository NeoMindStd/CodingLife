a,b=list(map(int,input().split())),list(map(int,input().split()))
sa=sb=0
for i in range(10):
    if a[i]>b[i]:sa+=3
    elif a[i]<b[i]:sb+=3
    else:
        sa+=1
        sb+=1
print(sa,sb)
if sa>sb:print('A')
elif sa<sb:print('B')
else:
    w='D'
    for i in range(9,-1,-1):
        if a[i]>b[i]:
            w='A'
            break
        elif a[i]<b[i]:
            w='B'
            break
    print(w)
