for T in range(int(input())):
    a,b=map(int,input().split())
    f=[500]+[300]*2+[200]*3+[50]*4+[30]*5+[10]*6
    s=[512]+[256]*2+[128]*4+[64]*8+[32]*16
    t=0
    if a!=0 and a<=len(f):t+=f[a-1]
    if b!=0 and b<=len(s):t+=s[b-1]
    print(t*10000)
