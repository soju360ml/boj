# 투포인터와 에라토스테네스의 체를 이용한 연속된 소수의 합 개수 찾기

import sys
input = sys.stdin.readline

# 최대값 입력 + 최대값이 곧 목표숫자
n = int(input())
source = [0]

if type(n) is int:
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False

    for i in range(2, n + 1):
        if sieve[i] is True:
            source.append(i)    # 소수 시퀀스 생성
            for j in range(i * 2, n + 1, i):
                sieve[j] = False

left, right = 0, 0
total = 0
count = 0

while True:
    if total >= n:
        if total == n and left != 0:    # 신묘한 트릭 left != 0
            count += 1
        total -= source[left]
        left += 1
    elif total < n:
        if right == len(source):
            break
        else:
            total += source[right]
            right += 1

print(count)