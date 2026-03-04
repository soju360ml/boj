# 시작점과 끝점이 연결된 순환 버퍼이므로 인덱스 테크닉을 이용해 순환하도록 한다
# 투 포인터 테크닉을 이용해 한 번의 시도에 가능한 최장거리를 탐색한다

import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())
ans = 0

circle = [None] * N
for i in range(N):
    circle[i] = int(input())

# 투포인터
left, right = 0, 0

