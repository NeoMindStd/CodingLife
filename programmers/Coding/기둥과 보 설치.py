def solution(n, build_frame):
    answer = []

    status = [[[0,0] for _ in range(n+1)] for _ in range(n+1)]
    #for row in status: print(*row)
    
    for build_info in build_frame:
        x, y, a, b = tuple(build_info)
        r, c = n-y, x
        #print(x, y, r, c, a, b)
        
        # 설치
        if b == 1:
            # 보
            if a == 1:
                # 왼쪽에 기둥이 있거나
                # 오른쪽에 기둥이 있거나
                # 양쪽이 보
                if status[r+1][c][0] == 1 or\
                   status[r+1][c+1][0] == 1 or\
                   (c > 0 and status[r][c-1][1] == status[r][c+1][1] == 1): 
                       status[r][c][a] = 1
            # 기둥
            else:
                # 설치 지점이 바닥일 때
                # 설치지점이 보의 한쪽 끝
                # 설치지점 아랫쪽이 기둥인 경우
                if r == n or\
                   ((c > 0 and status[r][c-1][1] == 1) ^ status[r][c][1] == 1) or\
                   status[r+1][c][0] == 1: 
                       status[r][c][a] = 1
                
        # 삭제
        else:
            # 보
            if a == 1:
                # 양쪽 모두 보로만 연결된 보가 아니고
                # 양쪽에 보가 없다면 양쪽 위에 기둥이 없어야 함
                if not(c > 0 and status[r][c-1][1] == 1 != status[r+1][c-1][0]) and\
                   not(status[r][c+1][1] == 1 != status[r+1][c+1][0]) and\
                   ((c > 0 and status[r][c-1][1] == 1) or (r == 0 or status[r-1][c][0] != 1)) and\
                   ((status[r][c+1][1] == 1) or (r == 0 or status[r-1][c+1][0] != 1)):
                    status[r][c][a] = 0
                   
            # 기둥
            else:
                # 위쪽에 기둥이 없어야 하고
                # 양쪽에 있는 보는 다른 보와 연결돼있거나 기둥이 있어야 
                if not status[r-1][c][0] == 1 and\
                   (status[r-1][c][1] == 0 or (c < n and status[r][c+1][0] == 1) or (0 < c < n and status[r-1][c-1][1] + status[r-1][c+1][1] == 2) ) and\
                   (c == 0 or status[r-1][c-1][1] == 0 or (status[r][c-1][0] == 1) or (1 < c and status[r-1][c-2][1] + status[r-1][c][1] == 2) ):
                    status[r][c][a] = 0
            
    #for row in status: print(*row)

    for x in range(n+1):
        for y in range(n+1):
            r, c = n-y, x
            for a in range(2):
                if status[r][c][a] == 1:
                    answer.append([x,y,a])
                
    
    return answer


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
