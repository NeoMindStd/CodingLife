import heapq
import sys;read=sys.stdin.readline
absHeap=[]
for i in range(int(read())):
    x=int(read())
    if x==0:
        try:
            t=heapq.heappop(absHeap)
            print(t[1])
        except: print(0)
    else:
        heapq.heappush(absHeap, (abs(x),x))
