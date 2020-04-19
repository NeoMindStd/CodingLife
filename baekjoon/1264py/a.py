while True:
    s=input().lower()
    if s=='#':break
    t=0
    for c in s:
        if c in ['a','e','i','o','u']: t+=1
    print(t)
