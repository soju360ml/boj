import sys
import collections
input = sys.stdin.readline
N, M = map(int, input().split())

adj = {}
inDegree = {}
que = collections.deque()
result = []
totalMember = set(range(1, N + 1))

for _ in range(M):
    p, n = map(int, input().split())

    if p not in adj: adj[p] = []
    if n not in adj: adj[n] = []
    if p not in inDegree: inDegree[p] = 0
    if n not in inDegree: inDegree[n] = 0
    adj[p].append(n)
    inDegree[n] += 1

for vertex in inDegree:
    totalMember.remove(vertex)
    if inDegree[vertex] == 0:
        que.append(vertex)

while que:
    node = que.popleft()
    result.append(node)
    
    for key in adj[node]:
        inDegree[key] -= 1
        if inDegree[key] == 0:
            que.append(key)

print(*result, *totalMember)