# 투포인터 사용

import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())

circle = [None] * N
for i in range(N):
    circle[i] = int(input())

q = deque()
cnt = 0
res = 0
checked = [0] * (d + 1)
bonus = False
for i in range(k):
    # print(f'현재 {circle[i]}입니다')
    cur = circle[i]
    q.append(cur)
    checked[cur] += 1
    if checked[cur] == 1:
        cnt += 1
    if i == k - 1 and checked[c] == 0:
        # print(f'현재 cnt: {cnt}')
        res = cnt + 1
    else:
        res = max(cnt, res)
    # print(res, '입니다')

# print('-' * 20)

for i in range(k, N + k):
    cur = circle[i % N]

    q.append(cur)
    out = q.popleft()

    checked[cur] += 1
    checked[out] -= 1

    if out != cur:
        if checked[cur] == 1:
            cnt += 1
        if checked[out] == 0:
            cnt -= 1
    
    if checked[c] == 0:
        res = max(res, cnt + 1)
    else:
        res = max(res, cnt)

print(res)