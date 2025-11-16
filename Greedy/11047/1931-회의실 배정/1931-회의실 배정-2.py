# 추가내용: 한 회의가 시작하자마자 끝나는 경우가 가능하다 예) 2 2 -> 2시시작하자마자 종료
# 1번 코드에서 안되는 반례
# 3, 1 2, 2 2, 2 3 = 3
# 3, 2 2, 1 2, 2 3 = 2
# 즉, 종료시간뿐만 아니라 시작시간도 오름차순으로 정렬해야함. 참조: https://dailyheumsi.tistory.com/67
# + 튜플끼리의 비교는 사전식 비교이다
#Job Scheduling#Greedy#Sort

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

schedule = [tuple(map(int, input().split())) for _ in range(N)]

# sort의 key매개변수를 통해 iterable 요소의 두번째 인덱스를 기준으로 정렬하도록 한다
schedule.sort(key=lambda x: (x[1], x[0]))
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