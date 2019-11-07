l1,l2=list(map(int,input().split())),list(map(int,input().split()))
print(max(max(l1[2],l2[2])-min(l1[0],l2[0]),max(l1[3],l2[3])-min(l1[1],l2[1]))**2)
