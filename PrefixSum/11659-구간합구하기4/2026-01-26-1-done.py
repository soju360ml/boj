from itertools import accumulate
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 원본 데이터를 입력받는 단계
source = [0] + list(map(int, input().split()))

# prefixSum 리스트를 생성
prefixSum = list(accumulate(source))

for i in range(M):
    l, r = map(int, input().split())
    print(prefixSum[r] - prefixSum[l - 1])