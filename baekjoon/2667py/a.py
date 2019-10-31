# 크기
n=int(input())
# 입력
h=[list(map(int,list(input()))) for _ in range(n)]
ra=range(n)

# 각 단지별 아파트 개수를 담을 배열
rs=[]
while True:
    stack = []
    # 순회하며 아직 체크해보지 않은 아파트가 있는지 검사합니다.
    for i in ra:
        for j in ra:
            # 하나라도 체크 안된게 있는 순간 스택에 해당 정보 삽입후 다음으로 진행
            if h[i][j]==1:
                h[i][j],tmp=2,[i,j,0, 0] # [행, 열, 방향, 방향시도횟수]
                stack.append(tmp)
                break
        if stack: break
    # 모두 체크되었다면 종료합니다
    if not stack: break
    # 현재 단지의 아파트 개수를 카운팅하는 변수
    cnt = 1
    while True:
        # 방향을 바꿔 시도해본 횟수가 4번 이하일 때 까지(0부터 시작하므로 이하)
        while tmp[3]<4:
            # 북쪽
            if tmp[2]==0 and tmp[0] > 0 and h[tmp[0]-1][tmp[1]] == 1:
                tmp = [tmp[0]-1, tmp[1], tmp[2], 0]
                stack.append(tmp)
                h[tmp[0]][tmp[1]]=2
                cnt+=1
                break
            # 동쪽
            elif tmp[2]==1 and tmp[1] < n-1 and h[tmp[0]][tmp[1]+1] == 1:
                tmp = [tmp[0], tmp[1]+1, tmp[2], 0]
                stack.append(tmp)
                h[tmp[0]][tmp[1]]=2
                cnt+=1
            # 남쪽
            elif tmp[2]==2 and tmp[0] < n-1 and h[tmp[0]+1][tmp[1]] == 1:
                tmp = [tmp[0]+1, tmp[1], tmp[2], 0]
                stack.append(tmp)
                h[tmp[0]][tmp[1]]=2
                cnt+=1
            # 서쪽
            elif tmp[2]==3 and tmp [1] > 0 and h[tmp[0]][tmp[1]-1] == 1:
                tmp = [tmp[0], tmp[1]-1, tmp[2], 0]
                stack.append(tmp)
                h[tmp[0]][tmp[1]]=2
                cnt+=1
            # 현재 진행방향이 가로막힌 경우
            else:
                # 다음 방향 시도, 방향을 바꿔 시도해본 횟수 +1
                tmp = [tmp[0], tmp[1], (tmp[2]+1)%4, tmp[3]+1]
        # 스택에 요소가 남은 경우 pop해서 다른방향으로 시도
        if stack:
            tmp=stack.pop()
        # 스택에 남은 요소가 없는 경우 단지를 모두 순회한 것으로 보고 다음 단지 탐색
        else:
            break
    # 현재 단지의 아파트 수를 결과 배열에 추가함
    rs.append(cnt)
# 결과 배열을 정렬
rs.sort()
# 단지 개수 출력
print(len(rs))
# 정렬된 상태의 단지 개수를 순서대로 출력
print("\n".join(map(str,rs)))
