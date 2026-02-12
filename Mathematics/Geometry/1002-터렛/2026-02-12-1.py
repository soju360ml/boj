import sys
import math
input = sys.stdin.readline

K = int(input())

def solve():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    diff = abs(r1 - r2)

    if dist == 0 and r1 == r2:
        print(-1)
    elif diff == dist or dist == r1 + r2:
        print(1)
    elif diff < dist < r1 + r2:
        print(2)
    else:
        print(0)

for _ in range(K):
    solve()