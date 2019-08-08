while(True):
    datas = list(map(int, input().split()))
    if(datas[0] == 0 and datas[1] == 0):
        break
    print(sum(datas))
