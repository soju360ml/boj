import sys
input = sys.stdin.readline

N, M = map(int, input().split())
source = list(map(int, input().split()))

left, right = 0, 0
total = 0
count = 0

while True:
    if total >= M:
        if total == M:
            count += 1
        total -= source[left]
        left += 1
    elif total < M:
        if right == N:
            break
        else:
            total += source[right]
            right += 1

print(count)