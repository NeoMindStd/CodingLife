a,b=map(int,input().split())
t=1 if b>0 else -1
print(a//(t*b)*t,a%(t*b),sep='\n')
