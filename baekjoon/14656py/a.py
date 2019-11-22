print(int(input())-len(list(filter(lambda x:x[0]+1==x[1],enumerate(map(int,input().split()))))))
