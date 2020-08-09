import sys

dic = dict()
for line in sys.stdin:
#for i in range(14):
 #   line=input()
    for c in line:
        if not(ord('a')<=ord(c)<=ord('z')):continue
        try:dic[c]+=1
        except:dic[c]=0
print(''.join(sorted(map(lambda x:x[0],filter(lambda x:x[1]==max(dic.items(),key=lambda x:x[1])[1],dic.items())))))
