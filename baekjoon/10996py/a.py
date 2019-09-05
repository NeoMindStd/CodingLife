n = int(input())

for i in range(n*2):
    for j in range(n):
        if i % 2 != 0:
            print(' ' if j % 2 == 0 else '*', end='')
        else:
            print('*' if j % 2 == 0 else ' ', end='')
    print()
