month = [0]+[30+(i%2) for i in range(1,8)]+[31-(i%2) for i in range(8,13)]
def calc_dyas(yyyy, mm, dd):
    feb = 28
    if yyyy % 400 == 0 or yyyy % 100 != 0 == yyyy % 4: feb += 1
    month[2] = feb

    return sum(month[:mm])+dd
    
while True:
    dd, mm, yyyy = map(int, input().split())
    if dd == mm == yyyy == 0: break
    print(calc_dyas(yyyy, mm, dd))
