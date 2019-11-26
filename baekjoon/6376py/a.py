a=[1,1]
while a[-1]<=10**9:
    a.append(a[-1]*len(a))
r=['n e','- -----------']
for i in range(2):
    s='%d %.0f' %(i, sum(map(lambda x: 1/x, a[:i+1])))
    r.append(s)
for i in range(2,3):
    s='%d %.1f' %(i, sum(map(lambda x: 1/x, a[:i+1])))
    r.append(s)
for i in range(3,10):
    s='%d %.9f' %(i, sum(map(lambda x: 1/x, a[:i+1])))
    r.append(s)
print('\n'.join(r))
