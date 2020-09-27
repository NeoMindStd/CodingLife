a, b, c = map(int, input().split())
ops = '+-*/'
answer = ''
for op in ops:
    if eval(f'{a}=={b}{op}{c}'): answer = f'{a}={b}{op}{c}'
    if eval(f'{a}{op}{b}=={c}'): answer = f'{a}{op}{b}={c}'
print(answer)
