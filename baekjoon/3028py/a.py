l=list(input())
c=[True,False,False]
def A(c):c[0],c[1]=c[1],c[0]
def B(c):c[1],c[2]=c[2],c[1]
def C(c):c[0],c[2]=c[2],c[0]
for s in l:exec(f'{s}(c)')
print(c.index(True)+1)
