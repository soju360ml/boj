# 시간초과
n = int(input())
prevTable = [0] * (n + 1)
number = list(map(int, input().split()))
prevTable[1:] = number
maxNum = max(prevTable)

for _ in range(1, n + 1):
    curTable = [0] * (n + 1)
    for i in range(1, n + 1):
        curTable[i] = prevTable[i - 1] + number[i - 1]
    maxNum = max(curTable) if max(curTable) > maxNum else maxNum
    prevTable = curTable
print(maxNum)