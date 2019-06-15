a = int(input())
b = list(input().split())

for i in range(len(b)):
    b[i] = int(b[i])


bsum = 0
for i in range(len(b)):
    bsum += b[i]/max(b)*100

print(bsum/len(b))
