# 메모리 초과
n = int(input())
numberList = list(map(int, input().split()))
table = [[0] * (n + 1) for _ in range(n + 1)]
maxNum = max(numberList)

for i in range(1, n + 1):
    for j in range(i, n + 1):
        table[i][j] = table[i - 1][j - 1] + numberList[j - 1]
        if table[i][j] > maxNum:
            maxNum = table[i][j]
print(maxNum)