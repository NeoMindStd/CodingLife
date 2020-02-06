input()
l=list(filter(lambda x:x>-1,map(int,input().split())))
print(sum(l)/len(l))
