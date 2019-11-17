a,b=map(list,input().split())
s=0;
dp={str(i):None for i in range(10)}
for aa in a:
    if dp[aa] is not None:
        s+=dp[aa]
        continue
    dp[aa]=0
    for bb in b:
        dp[aa]+=int(aa)*int(bb)
    s+=dp[aa]
print(s)
