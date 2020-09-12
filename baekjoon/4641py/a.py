while True:
    s = input()
    if s == '-1': break
    
    s = list(map(int, s.split()))

    c = 0

    for no in s[:-1]:
        if s.count(no*2) > 0: c += 1

    print(c)
