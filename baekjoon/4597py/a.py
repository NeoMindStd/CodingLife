while True:
    s=input()
    if s=='#':break
    r=0
    for c in s:
        if c=='1':r+=1
    r='0'if r%2==0 and s[-1]=='e' or r%2!=0 and s[-1]=='o' else '1'
    print(s[:-1]+r)
