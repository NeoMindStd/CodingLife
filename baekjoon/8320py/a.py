n=int(input())
s=0
for i in range(1, n+1):
    for j in range(1, int(i**.5)+1):
        if i%j==0: s+=1
print(s)
