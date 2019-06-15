import sys
sys.setrecursionlimit(10000)

n = int(input())

def count_hansu(n):
    if n > 0:
        sliced = list(map(int, list(str(n))))
        sub_before = -11
        for i, _ in enumerate(sliced):
            try:
                sub = sliced[i]-sliced[i+1]
                if(sub_before != -11 and sub != sub_before):
                    return count_hansu(n-1)
                sub_before = sub
            except IndexError:
                break
        return 1 + count_hansu(n-1)
    else:
        return 0

print(count_hansu(n))
