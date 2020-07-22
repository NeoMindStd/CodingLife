my=input()
n=int(input())
girls=[[[0,0,0,0],input()] for _ in range(n)]

l=o=v=e=0
for c in my:
    if c=='L': l+=1
    elif c=='O': o+=1
    elif c=='V': v+=1
    elif c=='E': e+=1

def calc(my,girl):
    l,o,v,e=my[0]+girl[0],my[1]+girl[1],my[2]+girl[2],my[3]+girl[3]
    return ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100

for girl in girls:
    for c in girl[1]:
        if c=='L': girl[0][0]+=1
        elif c=='O': girl[0][1]+=1
        elif c=='V': girl[0][2]+=1
        elif c=='E': girl[0][3]+=1
    girl[0]=-calc((l,o,v,e),girl[0])

girls.sort()
print(girls[0][1])
