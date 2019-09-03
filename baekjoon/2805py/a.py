import sys

n, m = map(int,sys.stdin.readline().split())
forest = list(map(int,sys.stdin.readline().split()))
answers = []

def fun(minn, maxx):
    summ = 0
    foo = (minn + maxx) // 2
    for tree in forest:
        summ += tree - foo if tree > foo else 0
        if summ > m:
            break
    if summ == m:
        return foo
    elif minn >= maxx:
        return max(answers)
    elif summ > m:
        answers.append(foo)
        return fun(foo+1, maxx)
    else:
        return fun(minn, foo)
            
print(fun(0, max(forest)))
