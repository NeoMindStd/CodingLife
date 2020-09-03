bowls = input()

h, c = 0, None
for bowl in bowls:
    if c==bowl: h+= 5
    else: h+= 10
    c = bowl
    
print(h)
