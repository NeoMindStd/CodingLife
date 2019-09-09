from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())

    start = n;
    end = n;
    sf = False
    ef = False

    while True:
        if not sf:
            sp = True
            for i in range(2, int(start**0.5)+1):
                sp = start % i != 0
                if not sp:
                    break
            sf = sp
                
        if not ef:
            ep = True
            for i in range(2, int(end**0.5)+1):
                ep = end % i != 0
                if not ep:
                    break
            ef = ep
        if sf and ef:
            break
        if not sf:
            start -= 1
        if not ef:
            end += 1
    print(end-start)
