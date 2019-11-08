a,b=list(map(int,input().split(' : '))),list(map(int,input().split(' : ')))
a,b=a[0]*3600+a[1]*60+a[2],b[0]*3600+b[1]*60+b[2]
if a>b:b+=86400
print(b-a)
