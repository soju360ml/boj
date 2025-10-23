# 전형적인 하노이탑 문제
# 횟수뿐만 아니라 이동경로도 출력해야한다

# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

"""
예제 입력1: 3
예제 출력1:
7
1 3
1 2
3 2
1 3
2 1
2 3
1 3
"""

# 실제로 탑을 저장할 데이터셋은 필요없다 -> 논리구조만 완벽하면 판때기의 개수만으로 계산할 수 있음
# 논리구조는 다음과 같다
# 1. 현재 이동을 원하는 판때기 위의 모든 판때기들을 임시버퍼에 이동시킨다
# 2. 이동을 원하는 판때기를 표적에 이동시킨다
# 3. 임시버퍼의 판때기를 표적에 이동시킨다

N = int(input())
pathOrder = []

def hanoi(판때기개수, 현재위치: int, 표적: int, 버퍼: int):
    global pathOrder
    count = 0

    if 판때기개수 == 1:
        count += 1
        pathOrder.append((현재위치, 표적))
        return count
    
    count += hanoi(판때기개수 - 1, 현재위치, 버퍼, 표적)
    count += 1
    pathOrder.append((현재위치, 표적))
    count += hanoi(판때기개수 - 1, 버퍼, 표적, 현재위치)
    return count

count = hanoi(N, 1, 3, 2)
print(count)
for i in pathOrder:
    print(*i)