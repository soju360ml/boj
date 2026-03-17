import sys; read = sys.stdin.readline

N, M = map(int, read().split())

lst = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    lst[i] = [0] + list(map(int, read().split()))

pos = [None] * M
for i in range(M):
    pos[i] = list(map(int, read().split()))

pSum = [[0] * (N + 1) for _ in range(N + 1)]

def prefixSum(lst, pSum):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            pSum[i][j] = pSum[i][j - 1] + pSum[i - 1][j] - pSum[i - 1][j - 1] + lst[i][j]
    
def rangeSum(lst_sum, pos):
    x1, y1, x2, y2 = pos
    res = lst_sum[x2][y2] - lst_sum[x2][y1 - 1] - lst_sum[x1 - 1][y2] + lst_sum[x1 - 1][y1 - 1]
    return res

prefixSum(lst, pSum)
for i in range(M):
    print(rangeSum(pSum, pos[i]))