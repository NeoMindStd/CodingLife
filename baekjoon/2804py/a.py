a,b=input().split()
s=[0,0]

for i in range(len(a)):
    try:
        s[1]=b.index(a[i])
        s[0]=i
        break
    except:pass

for i in range(len(b)):
    if i==s[1]:o=a
    else:
        o=''
        for j in range(len(a)):
            if j==s[0]:o+=b[i]
            else:o+='.'
    print(o)
