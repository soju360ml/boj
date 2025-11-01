# BFS는 최단경로 탐색을 할 수 있지만 모든 인접노드들을 순회하는 데에 활용될 수 있다
# 인접리스트의 모든 노드를 순회할 필요 없다 -> 감염이 이미 된 노드의 인접노드만 골라서 순회하면 된다

from collections import deque

N = int(input())
M = int(input())

adjacencyList = {}
for i in range(1, N + 1):
    adjacencyList[i] = set()

for _ in range(M):
    relation = tuple(map(int, input().split()))
    adjacencyList[relation[0]].add(relation[1])
    adjacencyList[relation[1]].add(relation[0])

que = deque()
que.append(1)
visited = set({1})
infected = set({1})

while que:
    curComputer = que.popleft()
    for adj in adjacencyList[curComputer]:
        if adj in visited:
            continue
        que.append(adj)
    visited.add(curComputer)

print(len(visited) - 1)