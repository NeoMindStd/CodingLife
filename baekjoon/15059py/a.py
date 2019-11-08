l1,l2=list(map(int,input().split())),list(map(int,input().split()))
def f(a,b):
    t=b-a
    return t if t>0 else 0
print(sum(map(lambda x: f(l1[x],l2[x]) ,[i for i in range(len(l1))])))
