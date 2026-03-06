# 시작점과 끝점이 연결된 순환 버퍼이므로 인덱스 테크닉을 이용해 순환하도록 한다
# 브루트 포스를 사용하여 오래 걸리는 코드 -> 백준 시간초과 -> 3.py 코드로 재구성

import sys
input = sys.stdin.readline

# 노드의 개수 N, 종류 d, 접시연속개수 k, 보너스 c
N, d, k, c = map(int, input().split())
ans = 0

circle = [None] * N
for i in range(N):
    circle[i] = int(input())


cnt = 0
for i in range(N):
    lst = [None] * k
    checked = [False] * (d + 1)
    tmpCnt = 0
    for j in range(k):
        type = circle[(i + j) % N]
        if checked[type] is False:
            # print(f'{type}은 존재하지 않습니다. {type}을 True로 변경합니다.')
            checked[type] = True
            tmpCnt += 1
            # print(tmpCnt, '입니다')
    cnt = max(cnt,tmpCnt)
    if tmpCnt == k and checked[c] is False:
        cnt += 1
        break

print(cnt)