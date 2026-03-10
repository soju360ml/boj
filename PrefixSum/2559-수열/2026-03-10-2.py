import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lst = [0] + list(map(int, input().split()))

sum_arr = [0] * (N + 1)

sum_arr[K] = sum(lst[1:K + 1])

for i in range(K + 1, N + 1):
    sum_arr[i] = sum_arr[i - 1] + lst[i] - lst[i - K]

print(max(sum_arr[K:]))