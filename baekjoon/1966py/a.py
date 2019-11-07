from sys import stdin
import collections
read=stdin.readline

for T in range(int(read())):
    n,m=map(int,read().split())
    l=list(map(int,read().split()))
    for i in range(n):
        l[i]=(i,l[i])
    Q=collections.deque(l)
    k=Q[m][0]
    i=0
    while True:
        if max(Q,key=lambda x:x[1])[1]>Q[0][1]:
            Q.append(Q.popleft())
            continue
        i+=1
        if Q.popleft()[0] == k:
            print(i)
            break
