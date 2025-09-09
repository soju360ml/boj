
# BOJ 11375
# Algorithm - Bipartite Matching
# DFS기반 포드-풀커슨 원리를 이용해 선점자의 매칭을 바꾸는 방식으로 증가경로를 늘려 최대 매칭 수를 찾는다
# 무한루프를 방지하기 위해 직원1에 해당하는 일거리 리스트에서 remove()를 해버리는 실수를 했다
# 이렇게 상위 노드의 경로재탐색이 불가능해짐
# 예시그래프) 1(a,b) 2(b,c) 3(c) 2-b 1-b 2-c 3-c 이후 2는 탐색실패(b가없음)
# 위 해결을 위해 visited는 한 사람의 탐색과정에서 일에 기록해야함
# 재귀방식으로 증가경로를 탐색한다

import sys
input = sys.stdin.readline

def match(adj):
    count = 0
    matching_node = {}
    matched_node = {}
    exception_1 = set()
    for node in adj:
        i = dfs(adj, node, exception_1, matching_node, matched_node)
        if i == True:
            count += 1
    return count

    #제외일거리에는 신규직원의 매칭도 제외해야함
def dfs(adj, node, exception, node_work, work_node):
        # 일거리가 매칭되면 참을 리턴한다, 반복문을 모두 진행시켜도 매칭되지 않으면 거짓을 리턴한다
        for work in adj[node][1]:
            #   5이미 매칭된 일자리가 아닌가?
            #   누구의 간섭도 받지 않고 해당 노드와 바로 매칭이 가능하므로 리턴!
            #   직원키일자리리스트, 일자리키직원값리스트에 현재노드, 매칭노드 업데이트
            #   리턴 참
            if work not in work_node:
                node_work[node] = work
                work_node[work] = node
                return True
            # 상위 신규직원이 탈취해야할 일자리이므로 기존직원은 그 일자리들을 무시해야한다
            # 이 제외일자리스트은 내부에서 재귀함수 호출 전에 업데이트한다(신규직원이 탈취해야할 일자리이므로)
            if work in exception:
                continue
            #   예를 들어 신규 직원이 이 일자리(일자리키직원값리스트에 포함된)를 탈취하려고 한다면
            #   그 일자리를 선점하고 있던 기존 직원을 다른 곳에 매칭시키도록 함수를 재귀시켜야한다
            #   이 조건문이 바로 재귀함수의 중심이다
            #   신규 직원이든 선점 직원이든 이 조건문을 통해 함수를 재귀시킨다

            #   2이미 일자리키직원값리스트에 포함되어있는가?:
            if work in work_node:
                #   누구 = 일자리키직원값리스트에서 찾아서 대입
                who = work_node[work]
                #   그 일자리는 선점될 예정임을 명시
                exception.add(work)
                #   재귀시켜서 경로를 찾는다
                result = dfs(adj, who, exception, node_work, work_node)
                #   결과가 참인가?
                if result == True:
                    #   재귀루프 탈출 후 결과가 참이면 해당 일자리는 탈취가 가능하므로 참 리턴
                    #   직원키일자리리스트, 일자리키직원값리스트에 현재노드, 매칭노드 업데이트
                    node_work[node] = work
                    work_node[work] = node
                    #   새로운 노드로 매칭이 완료되었으므로 예외에서 제거
                    exception.discard(work)
                    return True
                #   결과가 거짓인가?
                else:
                    #   현재 일자리에는 매칭시킬 수 없으므로 다른 일자리 매칭을 시도하기 위해 컨티뉴
                    #   = 현재 일자리는 경로증가를 찾을 수 없으므로 예외일자리셋에 등록
                    #   = 이미 사전등록 해놨으므로 따로 처리할 필요없음
                    # exception.add(work)
                    continue
        #   (반복문끝) -> 매칭 가능한 일자리 없음
        #   증가경로를 찾지 못했으므로 해당 노드는 어느 노드와도 매칭이 불가함
        return False
        
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
        # 정렬은 불필요하므로 주석처리
        # adjacency[i][1].sort()
        
    print(match(adjacency))