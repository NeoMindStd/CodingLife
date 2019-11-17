l=[]
for T in range(int(input())):
    n=int(input())
    r=('#'*n+'\n'+f'#{"J"*(n-2)}#\n'*(n-2)+'#'*n) if n>1 else '#'
    l.append(r)
print('\n\n'.join(l))
