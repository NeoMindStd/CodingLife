import sys;read=sys.stdin.readline
for T in range(int(read())):
    l=list(map(int,read().split()))
    s=set([])
    if l[0]!=l[1]:
        for y in range(1,min(l[4]//l[2],l[5]//l[3])+1):
            x=(l[4]-l[5]-(l[2]-l[3])*y)//(l[0]-l[1])
            if x!=0!=y and x*l[0]+y*l[2]==l[4]and x*l[1]+y*l[3]==l[5]:s.add((x,y))
    elif l[2]!=l[3]:
        for x in range(1,min(l[4]//l[0],l[5]//l[1])+1):
            y=(l[4]-l[5]-(l[0]-l[1])*x)//(l[2]-l[3])
            if x!=0!=y and x*l[0]+y*l[2]==l[4]and x*l[1]+y*l[3]==l[5]:s.add((x,y))
    else:
        for y in range(1,l[4]//l[2]+1):
            x=(l[4]-l[2]*y)//l[0]
            if x!=0!=y and x*l[0]+y*l[2]==l[4]and x*l[1]+y*l[3]==l[5]:s.add((x,y))
    print(*s.pop()if len(s)==1 else'?')
