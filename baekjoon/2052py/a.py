a="%.250f"%(2**-int(input()))
c=0
for i in range(len(a)):
    if a[len(a)-i-1]=='0':
        c+=1
    else:break
print(a[:len(a)-c])
