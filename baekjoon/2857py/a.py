l=[input()for _ in range(5)]
s=''
for i in range(5):
    if l[i].count('FBI')>0:s+=f'{i+1} '
print(s if s!='' else'HE GOT AWAY!')
