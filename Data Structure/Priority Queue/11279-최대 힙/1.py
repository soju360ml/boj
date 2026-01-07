# 파이썬 빌트인 모듈 heapq는 최소힙이므로 값을 음수로 바꿔서 우회하는 방법으로 최대힙을 구현하면 된다

import sys
import heapq

input = sys.stdin.readline

N = int(input())

rawData = [int(input()) for _ in range(N)]
myHeap = []

for i in rawData:
    if i == 0:
        if len(myHeap) > 0:
            print((-1) * heapq.heappop(myHeap))
        else:
            print(0)
    else:
        heapq.heappush(myHeap, (-1) * i)