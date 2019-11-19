x,y=map(int,input().split())
s=1000/y*x
for i in range(int(input())):
    x,y=map(int,input().split())
    s=min(1000/y*x,s)
print(s)
