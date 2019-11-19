q=[0]*5
for i in range(int(input())):
    x,y=map(int,input().split())
    if x==0 or y==0:q[0]+=1
    elif x>0 and y>0:q[1]+=1
    elif x<0 and y>0:q[2]+=1
    elif x<0 and y<0:q[3]+=1
    else:q[4]+=1
for i in range(1,5):
    print('Q%d: %d' %(i,q[i]))
print('AXIS:',q[0])
