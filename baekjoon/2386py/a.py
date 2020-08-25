while True:
    d=input()
    if d=='#':break
    a,p=d[:1],d[1:].lower()
    print(a, p.count(a))
