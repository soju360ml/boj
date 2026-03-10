# 인덱스 0을 고려하지 않고 sum을 구한 틀린 코드

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = [0] + list(map(int, input().split()))

pSum = [0] * len(lst)

for i in range(1, len(pSum)):
    pSum[i] = pSum[i - 1] + lst[i]

pSum.sort(reverse=True)

res = sum(pSum[1:K])

print(res)