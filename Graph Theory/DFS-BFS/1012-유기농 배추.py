# 2667과 유사
# 한 좌표를 기준으로 상하좌우 네 개의 인접 노드를 지정하는 방법
"""
for di,dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj= di+ci, dj+cj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:               
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj]+1

-> 결론적으로 하나하나 튜플을 만들어서 하나씩 연산한다
"""

from collections import deque

# 테스트 케이스 개수
T = int(input())

# 각 테스트 케이스 별 그룹의 수 테이블
the_num_of_groups = []

for _ in range(T):
    M, N, K = map(int, input().split())
    # 밭 테이블 0으로 init
    field = [[0] * M for _ in range(N)]

    # 배추가 심어진 좌표에 1값 assign
    for _ in range(K):
        i, j = map(int, input().split())
        field[j][i] = 1
    
    # 배추 집단의 개수
    count = 0
    
    diffNodeQue = deque()
    diffNodeQue.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    total = []
        
    while diffNodeQue:
        # 집단의 최초 셀
        curStart = diffNodeQue.popleft()
        if visited[curStart[0]][curStart[1]] == True:
            continue
        # 이 최초셀의 값(0또는1)
        curCellvalue = field[curStart[0]][curStart[1]]
        curQue = deque()
        curQue.append(curStart)
        
        # 현재집단이 끝날때까지 탐색
        while curQue:
            curCell = curQue.popleft()
            # 이미 방문한 셀이면 넘김
            if visited[curCell[0]][curCell[1]] == True:
                continue

            # 상하좌우 셀이 0인가 1인가?
            for i, j in (-1, 0), (0, -1), (0, 1), (1, 0):
                nextCell = curCell[0] + i, curCell[1] + j
                # 다음 셀이 인덱스를 벗어나지 않는지 검증
                if 0 <= nextCell[0] < N and 0 <= nextCell[1] < M:
                    if curCellvalue == field[nextCell[0]][nextCell[1]]:
                        curQue.append((nextCell))
                    else:
                        diffNodeQue.append(nextCell)
            visited[curCell[0]][curCell[1]] = True
        if curCellvalue == 1:
            count += 1
    the_num_of_groups.append(count)

for i in the_num_of_groups:
    print(i)