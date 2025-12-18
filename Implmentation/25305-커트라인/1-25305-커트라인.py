N, k = map(int, input().split())

dataList = list(map(int, input().split()))

print(sorted(dataList, reverse=True)[k - 1])