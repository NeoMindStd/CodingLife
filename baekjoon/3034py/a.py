n,w,h=map(int,input().split())
print('\n'.join([('NE'if int(input())>(w*w+h*h)**.5 else'DA')for _ in range(n)]))
