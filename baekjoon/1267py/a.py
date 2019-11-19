n=int(input())
l=list(map(int,input().split()))
y=m=0
for i in l:
    y+=10+i//30*10
    m+=15+i//60*15
if y>m:print('M',m)
elif y<m:print('Y',y)
else:print('Y M',y)
