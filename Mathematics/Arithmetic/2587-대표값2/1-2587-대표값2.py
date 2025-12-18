def mean(dataList: list):
    count = len(dataList)
    return int(sum(dataList) / count)

def median(dataList):
    middelIndex = (len(dataList) - 1) // 2
    return dataList[middelIndex]

numList = []
for _ in range(5):
    numList.append(int(input()))
    numList.sort()

print(mean(numList))
print(median(numList))