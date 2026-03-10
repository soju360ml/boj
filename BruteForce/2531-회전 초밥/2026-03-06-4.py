# 슬라이딩 윈도우 테크닉으로 해결한다
import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())

circle = [None] * N
for i in range(N):
    circle[i] = int(input())

ans = 0

for i in range(N):
    checked = [0] * (d + 1)
    cnt = 0
    for j in range(i, i + k):
        cur = circle[j % N]
        checked[cur] += 1
        if checked[cur] == 1:
            cnt += 1
    checked[c] += 1
    if checked[c] == 1:
        cnt += 1
    ans = max(ans, cnt)

print(ans)