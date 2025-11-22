# 시간초과
n = int(input())
numberList = list(map(int, input().split()))
prevTable = numberList.copy()
maxNum = max(prevTable)
for i in range(1, n):
    curTable = [0] * (n - i)
    length = len(curTable)
    for j in range(length):
        curTable[j] = prevTable[j] + numberList[i + j]
    m = max(curTable)
    if maxNum < m:
        maxNum = m
    prevTable = curTable
print(maxNum)