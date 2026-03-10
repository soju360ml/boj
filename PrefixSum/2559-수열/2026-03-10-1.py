# 시간초과

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = [0] + list(map(int, input().split()))

sum_arr = [0] * (N + 1)

for i in range(K, N + 1):
    sum_arr[i] = sum(lst[i - K + 1:i + 1])

print(max(sum_arr))