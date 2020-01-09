l=[int(input())]
while l[-1]!=1:
    if l[-1]%2==0:l.append(l[-1]//2)
    else:l.append(l[-1]*3+1)
print(*l)
