n, x = input().split()

x = int(x)

datas = list(map(int, input().split()))
             
for i in datas:
    if(i < x):
        print(i, end=' ')
