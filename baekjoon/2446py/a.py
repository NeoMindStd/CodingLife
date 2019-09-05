n = int(input())

for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(n-i)-1):
        print('*', end='')
    print()
    
for i in range(1, n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
