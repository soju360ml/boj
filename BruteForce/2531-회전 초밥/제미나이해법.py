import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())

circle = [0] * N
for i in range(N):
    circle[i] = int(input())

q = deque()
cnt = 0
res = 0
checked = [0] * (d + 1)

# 1. 초기 윈도우(0번부터 k-1번까지) 세팅
for i in range(k):
    cur = circle[i]
    q.append(cur)
    if checked[cur] == 0:  # 처음 보는 초밥이면 종류 증가
        cnt += 1
    checked[cur] += 1

# 초기 윈도우에서의 최댓값 계산 (보너스 초밥 c가 없다면 + 1)
if checked[c] == 0:
    res = cnt + 1
else:
    res = cnt

# 2. 슬라이딩 윈도우 진행 (1번 인덱스부터 시작)
for i in range(1, N):
    # ① 맨 앞쪽 노드 제거
    out = q.popleft()
    checked[out] -= 1
    if checked[out] == 0:  # 큐에서 완전히 빠졌으면 종류 감소
        cnt -= 1
    
    # ② 새로 들어올 노드 추가 (끝점 계산 주의!)
    # 시작점이 i이므로, 끝점은 i + k - 1 입니다.
    new_sushi = circle[(i + k - 1) % N]
    q.append(new_sushi)
    if checked[new_sushi] == 0:
        cnt += 1
    checked[new_sushi] += 1
    
    # ③ 보너스 초밥 판별 후 최댓값 갱신
    if checked[c] == 0:
        res = max(res, cnt + 1)
    else:
        res = max(res, cnt)
        
    # 최대치(k+1)에 도달했다면 더 이상 볼 필요 없으므로 종료
    if res == k + 1:
        break

print(res)