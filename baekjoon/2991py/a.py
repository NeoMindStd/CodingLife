a,b,c,d=map(int,input().split())
l=list(map(int,input().split()))
for ll in l:
    s=0
    if 0!=ll%(a+b)<=a:s+=1
    if 0!=ll%(c+d)<=c:s+=1
    print(s)
