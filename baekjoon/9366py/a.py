for T in range(int(input())):
    l=sorted(map(int,input().split()))
    if l[2]>=l[0]+l[1]:r='invalid!'
    elif l[2]==l[0]:r='equilateral'
    elif l[2]==l[1]or l[1]==l[0]:r='isosceles'
    else:r='scalene'
    print(f'Case #{T+1}: {r}')
