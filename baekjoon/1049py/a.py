n, m = tuple(map(int, input().split()))

packs = list()
eachs = list()

for T in range(m):
    pack, each = tuple(map(int, input().split()))
    packs.append(pack)
    eachs.append(each)
    
minPack = min(packs)
minEach = min(eachs)


if(minPack >= minEach*min(6, n)):
    print(n*minEach)
else:
    cntPack = n // 6
    cntEach = 0
    if(minPack <= (n%6)*minEach):
        cntPack+=1
    else:
        cntEach = n % 6
    print(cntPack * minPack + cntEach * minEach)
