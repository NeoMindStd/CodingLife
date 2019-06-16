n = list(map(int, input().split()))

mode = "mixed"
aFlag=True
bFlag=True
for i, ax in enumerate(n):
    if(i+1!=ax) : aFlag=False
    if(8-i!=ax) : bFlag=False
if(aFlag) : mode="ascending"
elif(bFlag) : mode="descending"
print(mode)
