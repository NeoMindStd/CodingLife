l=[[30,40],[35,30],[40,20]]
while True:
    a,b=map(int,input().split())
    if a==b==0:break
    print(min([i[0]*a+i[1]*b for i in l]))
