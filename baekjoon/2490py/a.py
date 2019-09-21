for _ in range(3):
    s = sum(map(int, input().split()))
    c = ""
    if s == 0:
        c = "D"
    elif s==1:
        c = "C"
    elif s==2:
        c = "B"
    elif s==3:
        c = "A"
    else:
        c = "E"
    print(c)
