N = int(input())
timeTable = list(map(int, input().split())) # list.sort()는 반환값 None이다
timeTable.sort()
sum = 0
for i, v in enumerate(timeTable):
    sum += v * (len(timeTable) - i)
print(sum)