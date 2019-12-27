l=[str(i) for i in range(1,int(input())+1)]
r=0
for i in l:
    for j in i:
        if j=='3'or j=='6'or j=='9':r+=1
print(r)
