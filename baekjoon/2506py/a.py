_,l=input(),input().split('0')
l=list(map(lambda x:x.split(), l))
for i in range(len(l)):
    t=sum(map(int,l[i]))
    l[i]=t*(t+1)//2
print(sum(l))
