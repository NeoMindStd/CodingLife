hs = [int(input()) for _ in range(9)]
hs.sort()

flag = False
for i1 in range(0, 3):
    for i2 in range(i1+1, 4):
        for i3 in range(i2+1, 5):
            for i4 in range(i3+1, 6):
                for i5 in range(i4+1, 7):
                    for i6 in range(i5+1, 8):
                        for i7 in range(i6+1, 9):
                            flag = (hs[i1]+hs[i2]+hs[i3]+hs[i4]+hs[i5]+hs[i6]+hs[i7] == 100)
                            if(flag): break
                        if(flag): break
                    if(flag): break
                if(flag): break
            if(flag): break
        if(flag): break
    if(flag): break


print(hs[i1])
print(hs[i2])
print(hs[i3])
print(hs[i4])
print(hs[i5])
print(hs[i6])
print(hs[i7])
