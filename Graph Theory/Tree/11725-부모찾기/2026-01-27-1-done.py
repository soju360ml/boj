# BFS를 통해 순회하기

import sys
from collections import deque
input = sys.stdin.readline

# 2 <= N <= 100_000
N = int(input())
edge = [tuple(map(int, input().split())) for _ in range(N - 1)]

myGraph = {}
for e in edge:
    n1, n2 = e  # 언패킹
    if n1 not in myGraph:
        myGraph[n1] = [n2]
    else:
        myGraph[n1].append(n2)
    if n2 not in myGraph:
        myGraph[n2] = [n1]
    else:
        myGraph[n2].append(n1)

visited = set()
myQueue = deque([1])
parents = [None] * (N + 1)  # 인덱스 = 노드번호

# BFS
while myQueue:
    node = myQueue.popleft()
    if node in visited:
        continue
    else:
        visited.add(node)
        for adj in myGraph[node]:
            if adj in visited:
                continue
            parents[adj] = node
            myQueue.append(adj)

for i in range(2, N + 1):
    print(parents[i])