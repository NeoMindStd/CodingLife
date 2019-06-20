for i in range(int(input())):
    a, b = tuple(map(int, input().split()))
    a-=1
    n = int(input())
    result = ""
    count = 0
    while result!="CORRECT":
        if count == n:
            print("WRONG_ANSWER")
            break
        count+=1
        answer = (a+b)//2 + (1 if (a+b)%2 != 0 else 0)
        print(answer)
        result = input()
        if result == "TOO_SMALL":
            a = answer
        elif result == "TOO_BIG":
            b = answer
