import sys
import collections

input = sys.stdin.readline
T = int(input())
totalResult = []

for _ in range(T):
    # 팀의 수 n
    teamCount = int(input())
    # 초기 순서
    order = list(map(int, input().split()))
    # Topology 변동개수
    c = int(input())
    changed = [tuple(map(int, input().split())) for _ in range(c)]
    que = collections.deque()
    result = []

    # Topology List 생성하기
    topology = {}
    degree = {}
    for k in order:
        topology[k] = set()
        degree[k] = 0

    for i, k in enumerate(order):
        for j in range(i + 1, len(order)):
            topology[k].add(order[j])
            degree[order[j]] += 1

    # 올 해 변동된 값대로 topology를 수정한다
    for p, n in changed:
        if n in topology[p]:
            topology[p].remove(n)
            topology[n].add(p)
            degree[p] += 1
            degree[n] -= 1
        else:
            topology[n].remove(p)
            topology[p].add(n)
            degree[n] += 1
            degree[p] -= 1

    for v in degree:
            if degree[v] == 0:
                que.append(v)
    if not que:
        result = 'IMPOSSIBLE'
    # 실제로 토폴로지와 in-degree값을 이용해 path를 구하는 부분
    while que:
        node = que.popleft()
        result.append(node)
        uncertainFlag = False

        for adj in topology[node]:
            degree[adj] -= 1
            if degree[adj] == 0:
                if uncertainFlag == True:
                    result = '?'
                    break
                que.append(adj)
                uncertainFlag = True
        if not que and len(result) != teamCount:
            result = 'IMPOSSIBLE'
    totalResult.append(result)
    
for i in totalResult:
    if i == 'IMPOSSIBLE':
        print(i)
    else:
        print(*i)