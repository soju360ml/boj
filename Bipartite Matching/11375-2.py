# BOJ 11375
# Algorithm - Bipartite Matching
# DFS기반 포드-풀커슨 원리를 이용해 선점자의 매칭을 바꾸는 방식으로 증가경로를 늘려 최대 매칭 수를 찾는다
# 무한루프를 방지하기 위해 직원1에 해당하는 일거리 리스트에서 remove()를 해버리는 실수를 했다
# 이렇게 상위 노드의 경로재탐색이 불가능해짐
# 예시그래프) 1(a,b) 2(b,c) 3(c) 2-b 1-b 2-c 3-c 이후 2는 탐색실패(b가없음)
# 위 해결을 위해 visited는 한 사람의 탐색과정에서 일에 기록해야함

import sys
input = sys.stdin.readline

def match(adj):
    count = 0
    match = {}
    match_work = {}
    for i in adj:
        if i in match:
            continue
        stack = [i]
        visited_work = set()
        cancel_flag = 0   # 신규직원이 일을 탈취했을 때 모든 선점자들이 새로운 일을 찾지 못한 경우 1
        while stack:
            node = stack.pop()
            for work in adj[node][1]:
                # 방문하지 않은 일이면 매칭
                if work not in visited_work:
                    visited_work.add(work)
                    match[node] = work
                    match_work[work] = node
                    count += 1
                    break
                else:
                    # 방문한 일일 경우-> 그 일에 해당하는 직원을 바꿔야함
                    if node in match:   # 현재 노드가 선점자일 경우 해당 일은 넘어간다(신규 직원이 탈취한 경우이므로)
                        continue
                    # 현재 직원이 해당 일을 선점하고 선점자를 스택에 넣어 다시 탐색하도록 한다
                    else:
                        visited_work.add(work)
                        stack.append(match)
                        del match[]
            if node not in 
                        
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