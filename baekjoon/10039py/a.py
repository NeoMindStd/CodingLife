n = [int(input()) for x in range(5)]
s=0
for i in n:
    if i > 40:
        s += i
    else :
        s += 40
print(s//5)

