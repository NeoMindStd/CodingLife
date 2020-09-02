for T in range(int(input())):
    l = input().split()
    acc = float(l[0])

    for i in range(len(l)):
        if l[i] =='@': acc *= 3
        elif l[i] =='%': acc += 5
        elif l[i] =='#': acc -= 7

    print('%.2f' %acc)
