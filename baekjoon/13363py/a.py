a,b=int(input()),int(input())
if b-a>180:s=b-a-360
elif b-a>-180:s=b-a
else:s=b-a+360
print(s)
