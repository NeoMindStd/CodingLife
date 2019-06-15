lane = list()
for i in range(8):
    lane.append(input())

white = 1
count = 0

for i in lane:
    for j in i:
        if(j=='F' and white==1):
            count += 1
        white = (white+1)%2
    white = (white+1)%2
print(count)
