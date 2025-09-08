# 과제1) dfs의 스택버전을 구현한다. 현재는 재귀함수로만 구현해놓음
# 과제2) 방문노드를 함수 내부에 캡슐화하여 전역변수 사용을 자제한다
# 이 그래프 탐색의 상위문제 1707

from collections import deque

N, M, V = map(int, input().split())

graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    graph[node].sort()
    
visited_bfs = set()
traversal_bfs = []

# def recursive_dfs(graph, start_node, visited_dfs):
#     visited_dfs.add(start_node)
#     traversal_dfs.append(start_node)
#     for neighbor in graph[start_node]:
#         if neighbor not in visited_dfs:
#             recursive_dfs(graph, neighbor, visited_dfs)

def recursive_dfs(graph, start_node, visited_dfs):
    visited_dfs = set()
    traversal_dfs = []

def bfs(graph, start_node, visited_bfs):
    visited_bfs.add(start_node)
    my_que = deque()
    my_que.append(start_node)
    while my_que:
        str_node = my_que.popleft()
        traversal_bfs.append(str_node)
        for i in graph[str_node]:
            if i in visited_bfs:
                continue
            visited_bfs.add(i)
            my_que.append(i)

recursive_dfs(graph, V, visited_dfs)
bfs(graph, V, visited_bfs)

print(*traversal_dfs)
print(*traversal_bfs)