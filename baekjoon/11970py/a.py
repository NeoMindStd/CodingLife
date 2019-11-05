a,b=map(int,input().split())
c,d=map(int,input().split())
l=[a,b,c,d]
if c<=a<=d or a<=c<=b:
    print(max(l)-min(l))
else:
    print(b-a+d-c)
