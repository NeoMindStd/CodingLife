days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

months = range(1, 13)
now = [1, 1]

mIn, dIn = input().split()
mIn = int(mIn)
dIn = int(dIn)

count = 1

pFlag = False;
for i in months:
    if(pFlag) :
        break
    
    now[0] = i
    
    if(i == 2):
        dd = range(1,29)
    elif ((i %2 == 0 and i < 7) or
        (i %2 != 0 and i > 7)):
        dd = range(1,31)
    else:
        dd = range(1,32)

    for j in dd:
        now[1] = j
        if(now[0] == mIn and now[1] == dIn):
            print(days[count%7])
            pFlag = True
            break
        count+=1
