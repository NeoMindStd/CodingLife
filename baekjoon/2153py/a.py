v=0
for c in input():
    o=ord(c)
    if o>=ord('a'): v+=o-ord('a')+1
    else: v+=o-ord('A')+1

f=True
for i in range(2,int(v**.5)+1):
    if v%i==0:
        f=False
        break
print('It is a prime word.'if f else 'It is not a prime word.')
