b,d,j=list(map(int,input().split())),list(map(int,input().split())),list(map(int,input().split()))
br = max(abs(b[0]-j[0]),abs(b[1]-j[1]))
dr = abs(d[0]-j[0])+abs(d[1]-j[1])
if br > dr:
    print("daisy")
elif br < dr:
    print("bessie")
else:
    print("tie")
