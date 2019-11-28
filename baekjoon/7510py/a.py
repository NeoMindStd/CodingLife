r=[]
for T in range(int(input())):
    l=sorted(map(int, input().split()))
    s=f'Scenario #{T+1}:'
    if l[2]**2==l[1]**2+l[0]**2:s+='\nyes'
    else:s+='\nno'
    r.append(s)
print('\n\n'.join(r))
