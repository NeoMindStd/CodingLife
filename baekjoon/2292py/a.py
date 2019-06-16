n = int(input())-2

pt=1
step=6
while(n>=0):
    pt += 1
    n -= step
    step += 6

print(pt)
