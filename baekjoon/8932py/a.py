s={'a':9.23076,'b':26.7,'c':1.835,'type':'t'},{'a':1.84523,'b':75,'c':1.348,'type':'f'},{'a':56.0211,'b':1.5,'c':1.05,'type':'f'},{'a':4.99087,'b':42.5,'c':1.81,'type':'t'},{'a':0.188807,'b':210,'c':1.41,'type':'f'},{'a':15.9803,'b':3.8,'c':1.04,'type':'f'},{'a':0.11193,'b':254,'c':1.88,'type':'t'}
for T in range(int(input())):
    l=list(map(int,input().split()))
    r=0
    for i in range(len(l)):
        if s[i]['type']=='t':r+=int(s[i]['a']*(s[i]['b']-l[i])**s[i]['c'])
        else:r+=int(s[i]['a']*(l[i]-s[i]['b'])**s[i]['c'])
    print(r)
