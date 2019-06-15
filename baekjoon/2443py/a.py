a = int(input())

for i in range(a):
    for j in range(i):
        print(" ", end="")
    for j in range(i, 2*a-i-1):
        print("*", end="")
    print()
