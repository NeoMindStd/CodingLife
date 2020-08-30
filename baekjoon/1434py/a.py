n, m = map(int,input().split())

boxes = list(map(int,input().split()))
books = list(map(int,input().split()))

i = j = 0
while i < n and j < m:
    if boxes[i] >= books[j]:
        boxes[i] -= books[j]
        j += 1
    else: i += 1
    
print(sum(boxes))
