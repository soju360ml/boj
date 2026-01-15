# 다익스트라
# 노드 A는 나머지 나머지 각각의 노드와 최단경로가 계산돼야 한다
# 방향그래프이다

import sys
# 다익스트라 구현을 위한 힙큐 자료구조 선택
import heapq
input = sys.stdin.readline

# 노드의 개수 V, 간선의 개수 E
V, E = map(int, input().split())

# 시작정점(기준정점)의 번호 K
K = int(input())

# 모든 노드를 키로써 딕셔너리를 생성한다
adj = {i: [] for i in range(1, V + 1)}

# 입력값을 토대로 노드와 간선을 연결짓는다; 횟수는 간선의 개수E
for _ in range(E):
    u, v, e = map(int, input().split())
    adj[u].append((v, e))

# 시작노드-나머지 각각의 노드간 최단경로; inf로 세팅한다
pathTable = {i: float('INF') for i in range(1, V + 1)}

# 최소힙으로 사용할 리스트 생성; 실제 힙 연산은 이 리스트를 토대로 heapq모듈을 사용하여 연산
minHeap = []

# 방문세트 생성; 사이클이 생기면 안 되므로
visited = set()

# 포인터 노드를 생성; 최초값은 입력으로 주어진 K노드로 세팅; 1번필드: 합계값, 2번필드: 현 노드번호
curNode = 0, K

# 다익스트라 시작
while curNode:
    # 방문 안 한 경우 처리진입 
    if curNode[1] not in visited:
        # 1. 방문처리
        visited.add(curNode[1])
        # 2. 이 노드 총 경로 확정; 인덱스 0은 합계경로
        pathTable[curNode[1]] = curNode[0]
        # 3. 이웃노드의 합산경로를 계산하여 힙큐에 추가
        for neighbor in adj[curNode[1]]:
            # 현재노드경로 + 다음노드가중치, 다음노드번호, 현재노드번호
            heapq.heappush(minHeap, (curNode[0] + neighbor[1], neighbor[0], curNode[1]))
    # 4. 최소힙에서 다음 노드 꺼내기
    if minHeap:
        curNode = heapq.heappop(minHeap)
    else:
        curNode = None

# 결과출력
for v in pathTable.values():
    if v == float('inf'):
        print('INF')
    else:
        print(v)