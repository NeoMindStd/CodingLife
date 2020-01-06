l=[k*(k+1)//2 for k in range(302)]
for T in range(int(input())):
    n=int(input())
    w=0
    for i in range(1,n+1):w+=i*l[i+1]
    print(w)
