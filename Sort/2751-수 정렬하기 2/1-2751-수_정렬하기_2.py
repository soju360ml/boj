N = int(input())

dataList = []
for _ in range(N):
    dataList.append(int(input()))
dataList.sort()
for i in dataList:
    print(i)