n,r=int(input()),""
for i in range(4,0,-1):r+=str(n//9**i);n%=9**i
r+=str(n)
print(int(r))
