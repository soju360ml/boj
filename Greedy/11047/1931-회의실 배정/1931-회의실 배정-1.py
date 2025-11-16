#Job Scheduling#Greedy#Sort

from collections import deque
N = int(input())

schedule = [tuple(map(int, input().split())) for _ in range(N)]

# sort의 key매개변수를 통해 iterable 요소의 두번째 인덱스를 기준으로 정렬하도록 한다
schedule.sort(key=lambda x: x[1])
que = deque(schedule)

# greedy알고리즘 사용, 종료시각이 가장 밭은 것이 최선의 선택
count = 0
curTime = 0
while que:
    # 가장 빠른 시간표
    nextSchedule = que.popleft()
    # 현재 진행중인 시간표의 종료시각이 가장 빠른 시간표의 시작시간보다 크면 패스
    if curTime > nextSchedule[0]:
        continue
    else:
        curTime = nextSchedule[1]
        count += 1

print(count)