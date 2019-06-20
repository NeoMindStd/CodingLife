n = int(input())

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    print("*", end="")
    for j in range(i):
        if i < n-1:
            print(" ", end="")
        else:
            print("*", end="")
    for j in range(i-1):
        if i < n-1:
            print(" ", end="")
        else:
            print("*", end="")
    if i!= 0 :
        print("*", end="")
    print()
