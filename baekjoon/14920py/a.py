l=[int(input())]
while l[-1]!=1:l.append(l[-1]//2if l[-1]%2==0else l[-1]*3+1)
print(len(l))
