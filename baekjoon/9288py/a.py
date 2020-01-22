for i in range(int(input())):
    n=int(input())
    print(f'Case {i+1}:')
    s=[]
    for i in range(max(1,n-6),min(n//2,12)+1):s.append(f'({i},{n-i})')
    print(*s,sep='\n')
