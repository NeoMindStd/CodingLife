n = int(input())
m = int(input())

l = list()

for _ in range(m):
    l.append(tuple(map(int, input().split())))

invited = set()
friends = set()

for a, b in l:
    if(a == 1):
        friends.add(b)
        invited.add(b)
    elif(b == 1):
        friends.add(a)
        invited.add(a)
    
for a, b in l:
    if(a in friends and b != 1):
        invited.add(b)
    elif(b in friends and a != 1):
        invited.add(a)
        
print(len(invited))
