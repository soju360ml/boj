# 시작점과 끝점이 연결된 순환 버퍼이므로 인덱스 테크닉을 이용해 순환하도록 한다
# 투 포인터 테크닉을 이용해 한 번의 시도에 가능한 최장거리를 탐색한다

import sys
from collections import deque
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())
ans = 0

circle = [None] * N
for i in range(N):
    circle[i] = int(input())

# 투포인터
left, right = 0, 0

seq = deque()
while left < N:
    if right == left:
        # 한 바퀴를 완전히 돈 경우
        if len(seq) > 1:
            # k(k<=N) 조건을 충족했으므로 보너스를 받는다
            if c in seq:    # 이미 c가 있는 경우 = N
                print(N)
            else:
                print(N + 1)    # c가 없는 경우 N + 1
        else:   # # 1칸도 진행하지 못한 경우
            seq.append(circle[left])
            right = (right + 1) % N
    else:
        while circle[right] in seq and left < N:
                seq.popleft()
                left += 1
                if left == N or left == right:
                    break
        seq.append(circle[right])
        right = (right + 1) % N
    if seq <= k:
        if c not in seq:
            seq.append(c)
            print('bonus')
    print(f'seq의 길이는 {len(seq)}이고 {seq}입니다')
    ans = max(ans, len(seq))

print(ans)