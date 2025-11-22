import sys
input = sys.stdin.readline

n = int(input())
prevTable = [0] * (n + 1)
number = list(map(int, input().split()))
maxNum = max(number)

for j in range(1, n + 1):
    curTable = [0] * (n + 1)
    for i in range(j, n + 1):
        curTable[i] = prevTable[i - 1] + number[i - 1]
        if maxNum < curTable[i]: maxNum = curTable[i]
    prevTable = curTable
print(maxNum)