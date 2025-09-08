# BOJ-1707
# 상위문제 BOJ-11375 열혈강호

import sys

input=sys.stdin.readline

# N: 정점의 개수
# M: 간선의 개수
# V: 시작 정점
K = int(input())
graph_list = []
result = []

def dfs(graph):
    stack = []
    flag = {i: 0 for i in range(1, len(graph) + 1)}
    for i in range(1, len(graph) + 1):
        if flag[i] == 0:
            flag[i] = 1
            stack.append(i)
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if flag[neighbor] == 0:
                        flag[neighbor] = -flag[node]
                        stack.append(neighbor)
                    elif flag[neighbor] == flag[node]:
                        return "NO"
    return "YES"

for i in range(K):
    N, M = map(int, input().split())
    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for j in graph:
        graph[j].sort()
        
    graph_list.append(graph)
    result.append(dfs(graph))

for i in range(K):
    print(result[i])