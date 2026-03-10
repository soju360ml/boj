# 슬라이싱 윈도우 테크닉으로 해결한다
import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())

circle = [None] * N
for i in range(N):
    circle[i] = int(input())

q = deque()
checked = [0] * (d + 1)
cnt = 0
tmpCnt = 0
size = 0
for i in range(N + k):
    curType = circle[i % N]
    q.append(curType)
    size += 1
    # 큐가 k를 초과하는 경우 1번 노드를 삭제한다
    if size > k:
        left = q.popleft()
        checked[left] -= 1
        # 삭제한 1번 노드가 큐의 고유한 노드였다면 카운트 1 감소
        if checked[left] == 0:
            tmpCnt -= 1
        size -= 1
    checked[curType] += 1
    if checked[curType] == 1:
        tmpCnt += 1
    if len(q) == k:
        tmpCnt += 1
    cnt = max(cnt, tmpCnt)

print(cnt)