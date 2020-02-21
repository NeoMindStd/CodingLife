def fact(n):return n*fact(n-1)if n>1 else 1
s=str(fact(int(input())))
for i in range(len(s)):
    if s[len(s)-i-1]!='0':break
print(i)
