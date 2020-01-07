a,b,c=input().split()
a=True if a=='true'else False
c=True if c=='true'else False
if b=='AND':print('true'if a and c else'false')
else:print('true'if a or c else'false')
