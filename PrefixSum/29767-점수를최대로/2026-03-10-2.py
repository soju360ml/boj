# sorted로 재정리한 코드(정답)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = [0] + list(map(int, input().split()))

pSum = [0] * len(lst)

for i in range(1, len(pSum)):
    pSum[i] = pSum[i - 1] + lst[i]

res = sum(sorted(pSum[1:], reverse=True)[:K])

print(res)