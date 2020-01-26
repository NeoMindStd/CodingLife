s=[0]
for T in range(int(input())):
    a,b,c,d=map(float,input().split())
    if (a>56 or b>45 or c>25)and a+b+c>125 or d>7:s.append('0')
    else:
        s.append('1')
        s[0]+=1
print('\n'.join(s[1:]+[str(s[0])]))
