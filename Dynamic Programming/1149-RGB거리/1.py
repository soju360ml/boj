N = int(input())
source = [[0] * 3 for _ in range(N + 1)]
for i in range(1, N + 1):
    source[i][:] = map(int, input().split())

for i in range(1, N + 1):
    curHouse = source[i].copy()
    for j in range(3):
        m = float('inf')
        flag = 0
        for k, value in enumerate(source[i - 1]):
            if k == j: continue
            else:
                if value < m:
                    flag = k
                    m = value
        source[i][j] = curHouse[j] + m
print(min(source[-1]))