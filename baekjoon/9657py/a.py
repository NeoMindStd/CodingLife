n=int(input())
l=[False]*(n+1)
for i in range(n):
    try:
        if not l[i]:
            l[i+1]=True
            l[i+3]=True
            l[i+4]=True
    except:pass
print('SK'if l[-1]else'CY')
