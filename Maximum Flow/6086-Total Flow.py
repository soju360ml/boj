"""
BOJ 6086 최대유량
"""
import sys  # sys.stdin.readline 사용
from collections import deque   # BFS 증가경로 탐색을 위한 큐

input = sys.stdin.readline  # input을 대체한다 -> 백준에서 input은 시간초과의 요인이 될 수 있음

# A-Za-z를 입력받아 인덱스로 변환하는 함수
# A-Z: 0~25
# a-z: 26~51
# 리턴은 인덱스
def map_char_to_index(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A')
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a') + 26
    else:
        raise Exception("잘못된 문자 입력")
        
# 간선의 개수를 전달받아 네트워크를 형성하는 함수
# 리턴은 인접리스트, 용량행렬
def create_network(line):
    # node는 딕셔너리를 이용한 인접리스트이다.
    # capacity는 딕셔너리를 이용한 용량행렬이다.
    adjacency = {}  # {None: {}}
    capacity = {}
    result_min = -1
    result_max = -1
    for _ in range(line):
        u, v, c = input().split()
        u, v = map(map_char_to_index, (u, v))
        c = int(c)
        
        result_min = min(u, v) if result_min == -1 else min(result_min, u, v)
        result_max = max(u, v) if result_max == -1 else max(result_max, u, v)

        adjacency.setdefault(u, []).append(v) # 인접리스트 생성
        adjacency.setdefault(v, []).append(u)
        """
        인접리스트 구현을 한 아래 코드를
        setdefault를 이용하여 대체한다; 결과는 위 2개 라인
        +setdefault메소드를 이용하면 딕셔너리의 키유무, 값생성코드를 따로 쓰지않아도 된다.

        if i not in adjacency:
            adjacency[i] = [j]
        elif i in adjacency:
            adjacency[i].append(j)
        if j not in adjacency:
            adjacency[j] = [i]
        elif j in adjacency:
            adjacency[j].append[i]
        if i not in capacity:
            capacity[i] = {}
        """

        # 백준문제는 A B 10  한줄에 양방향
        capacity.setdefault(u, {}).setdefault(v, 0)  # 딕셔너리 정방향 용량행렬
        capacity.setdefault(v, {}).setdefault(u, 0)  # 딕셔너리 역방향 용량행렬
        capacity[u][v] += c
        capacity[v][u] += c
    return adjacency, capacity, result_min, result_max

def max_flow(adjacency, capacity, source, sink):
    residual_capacity = {} # 잔여용량 행렬
    """for u in adjacency:
        for v in adjacency[u]:
            residual_capacity.setdefault(u, {})[v] = capacity[u][v] #정방향
            residual_capacity.setdefault(v, {})[u] = 0  #역방향
    """
    flow = {}   # 유량 행렬(0으로 초기화)
    
    for u in capacity:
        for v in capacity[u]:
            residual_capacity.setdefault(u, {})[v] = capacity[u][v] #정방향
            if not residual_capacity.setdefault(v, {}).get(u, False):
                residual_capacity[v][u] = 0
            #residual_capacity.setdefault(v, {})[u] = 0  #역방향-이 라인대로 작성하면
            #용량행렬에서 역방향데이터가 있을 시 0으로 덮어쓰기될 수 있음
            #예시 capacity[A][B] = 10 capacity[B][A] = 5일경우
            #ab10 ba0 이후 ba5 ab0처럼 ab가 덮어쓰기됨
    for u in adjacency:
        for v in adjacency[u]:
            flow.setdefault(u, {})[v] = 0
            flow.setdefault(v, {})[u] = 0

    max_flow = 0

    while True:
        queue = deque([source])
        parent = {source: None}

        #증가경로탐색을 시작한다
        while queue:
            u = queue.popleft()
            for v in residual_capacity[u]:
                #parent.get(v, None) == None대체
                if v not in parent and residual_capacity[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        
        # 싱크를 발견하지 못했다면 증가경로 탐색을 종료한다
        if sink not in parent:
            break

        # 싱크까지 도달하여 증가경로를 발견했다면 병목유량을 찾습니다
        path_flow = float("inf")
        
        v = sink
        while v != source:
            path_flow = min(path_flow, residual_capacity[parent[v]][v])
            v = parent[v]
        
        max_flow += path_flow

        # 잔여유량계산한다. 정방향 역방향 모두 업데이트한다
        v = sink
        while v != source:
            flow[parent[v]][v] += path_flow
            flow[v][parent[v]] -= path_flow
            residual_capacity[parent[v]][v] -= path_flow
            residual_capacity[v][parent[v]] += path_flow
            v = parent[v]

    return max_flow

if __name__ == "__main__":  # 채점을 위한 입력값 전용 스코프. 모듈과 분리하기 위함
    #간선의 개수
    N = int(input())
    adjacency, capacity, s, t = create_network(N)
    """
    예시입력:
    노드1 노드2 용량
    A B 3
    B C 3
    C D 5
    D Z 4
    B Z 6
    """
    print(max_flow(adjacency, capacity, 0, ord('Z') - ord('A')))