N = int(input())
rawTarget = tuple(map(int, input().split()))
targetTable = {}

M = int(input())
data = list(map(int, input().split()))
result = [0] * M

for i in rawTarget:
    if i in targetTable:
        targetTable[i] += 1
    else:
        targetTable[i] = 1

for i, value in enumerate(data):
    if value in targetTable:
        result[i] = targetTable[value]

print(*result)