l=[int(input())for _ in range(int(input()))]
s=set([i+1 for i in range(max(l))])
s=sorted(s-set(l))
print('\n'.join(map(str,s))if s else'good job')
