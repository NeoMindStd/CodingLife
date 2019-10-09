t = []
s = input().split(":")
t.append(int(s[0])*3600 + int(s[1])*60 + int(s[2]))
s = input().split(":")
t.append(int(s[0])*3600 + int(s[1])*60 + int(s[2]))

if len(t) == 1:
    t.append(t[0])
elif t[0] <= t[1]:
    t[0] += 86400

sec = 86400 - (t[0] - t[1])
time = []
time.append(str("%02d" %(sec//3600)))
sec %= 3600
time.append(str("%02d" %(sec//60)))
sec %= 60
time.append(str("%02d" %(sec)))
print(":".join(time))
