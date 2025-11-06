# 이 문제는 더 효율적인 정렬을 통해 해결할 수 있도록 한다. (2025-11-06)
N = int(input())
strList = []
for _ in range(N):
    ss = input()
    if len(strList) == 0:
        strList.append(ss)
    for index, i in enumerate(strList):
        if len(ss) < len(i):
            strList.insert(index, ss)
            break
    if index == len(strList):
        