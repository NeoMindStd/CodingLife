n = int(input())-1

si = 0
i = 0
while n >= si:
    i += 1
    si += i
b = si - n
a = i + 1 - b

if i%2 == 1:
    a, b = b, a

print(str(a)+"/"+str(b))

