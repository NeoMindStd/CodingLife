a = int(input())

aDiv5 = a // 5

flag = False

for i in range(aDiv5, -1, -1):
    ami = a-(i*5)
    amiDiv3 = ami // 3

    for j in range(amiDiv3, -1, -1):
        if(i*5 + j*3 == a):
            print(i+j)
            flag = True
            break
        
    if(flag):
        break
        
if(not flag):
    print(-1)
