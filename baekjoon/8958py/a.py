n = int(input())

for i in range(n):
    test = input()
    score = 0
    for a, ox in enumerate(test):
        if ox=="O":
            s = 1
            while(a-s>=0):
                if(test[a-s]=="O"):
                    s+=1
                    continue
                break
            score+=s
    print(score)
