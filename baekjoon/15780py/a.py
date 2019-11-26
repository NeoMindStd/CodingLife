n,k=map(int,input().split())
print('NO'if n>sum(map(lambda x: x//2+x%2, list(map(int,input().split())))) else'YES')
