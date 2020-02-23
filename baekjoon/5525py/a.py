n,m,s=int(input()),int(input()),input()
c,f,l='I',False,[]
i=r=0
while i<m:
    if s[i]==c:
        if f:l[-1][-1]+=1
        else:
            l.append([i,i+1])
            f=True
        c='O'if c=='I' else'I'
    else:
        if f:
            if s[i-1]=='O':l[-1][-1]-=1
            else:i-=1
            c='I'
            f=False
    i+=1
for i in l:r+=max((i[1]-i[0]+1-n*2)//2,0)
print(r)
