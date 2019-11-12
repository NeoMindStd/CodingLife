l=[list(map(int,input().split()))for _ in range(int(input()))]
def v(l):
    if l[0]==l[1]==l[2]:return 10000+l[0]*1000
    elif l[0]!=l[1]!=l[2]!=l[0]:return max(l)*100
    else: return 1000+(l[0]if l[0]==l[1] or l[0]==l[2] else l[1])*100
print(max(map(v, l)))
