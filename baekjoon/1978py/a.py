a = int(input())
datas = input().split()
datas = list(datas)

count = 0
for i in datas:
    i = int(i)
    flag = True
    for j in range(2,i//2+1):
        if(i%j == 0):
            flag = False
            break
    if(flag and i > 1):
        count+=1
print(count)
