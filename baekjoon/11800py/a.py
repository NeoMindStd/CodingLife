d=['',"Yakk","Doh","Seh","Ghar","Bang","Sheesh"]
dd=['',"Habb Yakk","Dobara","Dousa","Dorgy","Dabash","Dosh"]
for T in range(int(input())):
    a,b=map(int,input().split())
    a,b=max(a,b),min(a,b)
    r=f'Case {T+1}: '
    if a==b:r+=dd[a]
    elif a==6 and b==5:r+="Sheesh Beesh"
    else:r+=f'{d[a]} {d[b]}'
    print(r)
