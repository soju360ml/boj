# BOJ 11375
# Algorithm - Bipartite Matching
# DFS기반 포드-풀커슨 원리를 이용해 선점자의 매칭을 바꾸는 방식으로 증가경로를 늘려 최대 매칭 수를 찾는다

import sys
input = sys.stdin.readline

def match(adj):
    stack = []
    match = {}
    count = 0
    visited = set()

    for i in adj:
        if i not in visited:
            stack.append(i)
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for j in adj[node][1]:
                        if j not in match.values():
                            match[node] = j
                            adj[node][1].remove(j)
                            count += 1
                        else:
                            k = next((k for k, v in adj.items() if v == j), None)
                            if k:
                                match[node] = j
                                del match[k]
                                stack.append(k)
                                visited.discard(k)
    return count

if __name__ == "__main__":
    # N: 사람 수
    # M: 일의 개수
    N, M = input().split()
    N = int(N)
    M = int(M)

    """
    ex) adjacency = {
        1: [2, [A, B]],
        2: [2, [A, C]],
        3: [1, [C]]
        }
    """
    adjacency = {}
    for i in range(N):
        tmpInput = input().split()
        adjacency[i] = [tmpInput[0], tmpInput[1:]]
        adjacency[i][1].sort()
        
    print(match(adjacency))