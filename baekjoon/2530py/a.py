t = list(map(int, input().split()))
time = t[0]*3600+t[1]*60+t[2]+int(input())
time%=24*3600
t[0]=time//3600
time%=3600
t[1]=time//60
t[2]=time%60
print(*t)
