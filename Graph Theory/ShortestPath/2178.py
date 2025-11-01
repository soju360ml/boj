# 가중치가 1인 다익스트라
# 인접리스트가 필요없이 상하좌우로 접근하면 된다(인접리스트 제외)
# 경로비용만 계산하면 되므로 부모노드는 알 필요가 없다(parent table 제외)
# 경로비용테이블만 필요

# 입력 경로비용테이블, 방문노드테이블
def next(costs, visited) -> tuple:
    tmpCost = float('inf')
    row, column = None, None
    # 경로비용테이블의 모든 값 중 최소값인 노드를 찾아라
    # 경로비용테이블은 2차원 리스트이다
    for i in range(len(costs)):
        for j in range(len(costs[0])):
            if costs[i][j] < tmpCost and visited[i][j] is not True:
                tmpCost = costs[i][j]
                row, column = i, j
    return row, column

# 다익스트라 구현부
def Dijkstra() -> int:
    N, M = map(int, input().split())
    # 공백없는 문자열을 리스트에 각각 대응한다
    maze = [[None] * M for _ in range(N)]
    for i in range(N):
        tmpRow = input()
        for j in range(M):
            maze[i][j] = int(tmpRow[j])
    # 경로비용테이블
    costs = [[float('inf')] * M for _ in range(N)]
    costs[0][0] = 1
    # 방문노드테이블
    visited = [[False] * M for _ in range(N)]

    node = 0, 0
    while node[0] is not None and node[1] is not None:
        curRow = node[0]
        curColumn = node[1]
        cost = costs[curRow][curColumn]

        up = curRow - 1, curColumn
        down = curRow + 1, curColumn
        left = curRow, curColumn - 1
        right = curRow, curColumn + 1
        
        direct = [up, down, left, right]

        # 각 인접노드가 지금보다 싼 경로가 있는 경우만 갱신
        for i in direct:
            tmpRow, tmpColumn = i[0], i[1]
            if tmpRow >= 0 and tmpColumn >= 0 and tmpRow < len(costs) and tmpColumn < len(costs[0]):
                if maze[tmpRow][tmpColumn] == 1:
                    if cost + 1 < costs[tmpRow][tmpColumn]:
                        costs[tmpRow][tmpColumn] = cost + 1
        
        visited[curRow][curColumn] = True
        node = next(costs, visited)
    return costs[-1][-1]
    
result = Dijkstra()
print(result)