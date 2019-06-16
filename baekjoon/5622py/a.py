time = 0
for ch in input():
    pos = ord(ch)
    if ord(ch) > ord('R'):
       pos-=1
    if ord(ch) > ord('W'):
       pos-=1
    time += 3+((pos-ord('A'))//3)
print(time)
