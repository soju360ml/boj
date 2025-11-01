# BFS - 단지의 수와 해당 단지에 포함된 가구수 테이블 필요
# 현재 단지가 0인지 1인지로 구분하여 탐색한다
# 다른 단지값일 때 상위큐에 좌표를 기록
# 현재 단지값일 때 순회 -> 현재 단지 모든 가구 조사 후 상위큐에서 꺼내서 인접단지 조사 반복

from collections import deque

N = int(input())
houseTable = [[int(x) for x in input()] for _ in range(N)]

diffNodeQue = deque()
diffNodeQue.append((0, 0))
visited = [[False] * N for _ in range(N)]
total = []
    
while diffNodeQue:
    curStart = diffNodeQue.popleft()
    if visited[curStart[0]][curStart[1]] == True:
        continue
    curNumber = houseTable[curStart[0]][curStart[1]]
    curQue = deque()
    curQue.append(curStart)
    houseCount = 0
    while curQue:
        curNode = curQue.popleft()
        if visited[curNode[0]][curNode[1]] == True:
            continue
        right = (curNode[0], curNode[1] + 1)
        down = (curNode[0] + 1, curNode[1])
        left = (curNode[0], curNode[1] - 1)
        up = (curNode[0] - 1, curNode[1])
        if right[0] < N and right[1] < N:
            if  curNumber == houseTable[right[0]][right[1]]:
                curQue.append(right)
            else:
                diffNodeQue.append(right)
        
        if down[0] < N and down[1] < N:
            if curNumber == houseTable[down[0]][down[1]]:
                curQue.append(down)
            else:
                diffNodeQue.append(down)
        if left[0] >= 0 and left[1] >= 0:
            if curNumber == houseTable[left[0]][left[1]]:
                curQue.append(left)
            else:
                diffNodeQue.append(left)
        if up[0] >= 0 and up[1] >= 0:
            if curNumber == houseTable[up[0]][up[1]]:
                curQue.append(up)
            else:
                diffNodeQue.append(up)

        houseCount += 1
        visited[curNode[0]][curNode[1]] = True
    if curNumber == 1:
        total.append(houseCount)

print(len(total))
total.sort()
for i in total:
    print(i)