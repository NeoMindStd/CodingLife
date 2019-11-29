l=list(input())
c=[1,0,0,2]
def A(c):c[0],c[1]=c[1],c[0]
def B(c):c[0],c[2]=c[2],c[0]
def C(c):c[0],c[3]=c[3],c[0]
def D(c):c[1],c[2]=c[2],c[1]
def E(c):c[1],c[3]=c[3],c[1]
def F(c):c[2],c[3]=c[3],c[2]
for s in l:exec(f'{s}(c)')
print(f'{c.index(1)+1}\n{c.index(2)+1}')
