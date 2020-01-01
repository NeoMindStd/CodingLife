s=input()
l=[]
for i in range(len(s)):
    l.append(s[i:])
l.sort()
print('\n'.join(l))
