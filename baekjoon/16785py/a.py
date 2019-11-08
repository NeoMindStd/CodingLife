a,b,c=map(int,input().split())
d,i=0,0
while d<c:
    i+=1
    d+=a+(b if i%7==0 else 0)
print(i)
