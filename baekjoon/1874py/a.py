from sys import stdin
read=stdin.readline
n=int(read())
l,num=[int(read()) for _ in range(n)],[n-i for i in range(n)]
stack,r=[],[]

i=0
while i < n:
    while num and num[-1] <= l[i]:
        stack.append(num.pop())
        r.append('+')
    tmp = stack.pop()
    if tmp != l[i]:
        r=['NO']
        break
    r.append('-')
    i+=1

print('\n'.join(r))
