# 슬라이싱 윈도우 테크닉으로 해결한다
import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())
ans = 0

circle = [None] * N
for i in range(N):
    circle[i] = int(input())

q = deque()
for i in range(N + k):
    curType = circle[i % N]
    if curType