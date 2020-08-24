import sys;read=sys.stdin.readline
import collections

n = int(read())
fishes = [list(map(int,read().split())) for _ in range(n)]

q = collections.deque([])
enQ = q.append
deQ = q.popleft

directions = [(-1, 0),(0, -1),(0, 1),(1, 0)]

inserted = [[[999_999]*n for i in range(n)] for j in range(400)]

for i in range(n):
    for j in range(n):
        if fishes[i][j] == 9:
            fishes[i][j] = 0
            inserted[0][i][j] = 0
            enQ({'i':i,'j':j,'size':2,'eat':0,'time':0,'eaten':set([])})
            break
    if q: break


eatLog = (2,0,0)
cnt = 0
while q:
    cnt += 1
    current = deQ()
    for direction in directions:
        i,j = current['i']+direction[0],current['j']+direction[1]
        size, eat, time, eaten = current['size'], current['eat'], current['time'], current['eaten']
        
        if 0<=i<n and 0<=j<n and inserted[len(eaten)][i][j] > time and 0 <= fishes[i][j] <= size:
            time += 1
            inserted[len(eaten)][i][j] = time
            
            if (i,j) not in eaten and 0 < fishes[i][j] < size:
                while q and (q[0]['size'],q[0]['eat'],-q[0]['time']) >= (size,eat,-time):deQ()
                eat += 1
                eaten = eaten|set([(i,j)])
                inserted[len(eaten)][i][j] = time
                eatLog=max(eatLog,(size,eat,-time))
                print(i,j,(size,eat,-time))
                if eat >= size:
                    size += 1
                    eat = 0
            enQ({'i':i,'j':j,'size':size, 'eat':eat, 'time':time, 'eaten':eaten})
            #print(current, i,j)
print(-eatLog[2])
