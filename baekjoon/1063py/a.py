k,s,n=input().split()

k,s,n=list(k),list(s),int(n)
k,s=(ord(k[0])-ord('A')+1,int(k[1])),(ord(s[0])-ord('A')+1,int(s[1]))

def move(x,y):
    global k,s
    tk,ts=(k[0]+x,k[1]+y),s
    if tk==s: ts=(s[0]+x,s[1]+y)
    if (0 < tk[0] <= 8) and (0 < tk[1] <= 8) and\
       (0 < ts[0] <= 8) and (0 < ts[1] <= 8): k,s=tk,ts
        

for i in range(n):
    command=input()
    if command == 'R': move(1,0)
    elif command == 'L': move(-1,0)
    elif command == 'B': move(0,-1)
    elif command == 'T': move(0,1)
    elif command == 'RT': move(1,1)
    elif command == 'LT': move(-1,1)
    elif command == 'RB': move(1,-1)
    elif command == 'LB': move(-1,-1)

k,s=(chr(k[0]+ord('A')-1),str(k[1])),(chr(s[0]+ord('A')-1),str(s[1]))
k,s=''.join(k),''.join(s)

print(k)
print(s)
