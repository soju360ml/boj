# 시간초과
# 1. 원본수정 sort() -> 새 리스트 sorted()
# 2. list가 아니라 중복되지 않으므로 set으로 구성하여 상수시간으로 탐색한다


N, M = map(int, input().split())
듣잡 = set()
보잡 = set()
듣보잡 = list()
for _ in range(N):
    듣잡.add(input())
for _ in range(M):
    보잡.add(input())

# O(n ** 2)이 아니라 상수시간 O(1) : hasing을 이용해 바로 찾는다
for i in 듣잡:
    if i in 보잡:
        듣보잡.append(i)

print(len(듣보잡))
# join으로 할 경우 새 리스트를 만들어야하므로 오버헤드가 존재한다. print로 단순출력을 하도록 한다
print('\n'.join(sorted(듣보잡)))