while True:
    a=input()
    if a=='#':break
    a=list(map(lambda c:{'-':0,'\\':1,'(':2,'@':3,'?':4,'>':5,'&':6,'%':7,'/':-1}[c],a))
    s=0
    for i in range(len(a)):s+=a[len(a)-i-1]*8**i
    print(s)
