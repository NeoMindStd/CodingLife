tt=list(list(map(int,input().split())) for _ in range(3))
for t in tt:
    r=t[3]*3600+t[4]*60+t[5]-(t[0]*3600+t[1]*60+t[2])
    print(r//3600,(r%3600)//60,r%60)
