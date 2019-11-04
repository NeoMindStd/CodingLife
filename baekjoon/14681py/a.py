x,y=int(input()),int(input())
if x>0 and y>0:
    r=1
elif x>0 and y<0:
    r=4
elif x<0 and y>0:
    r=2
else:
    r=3
print(r)
