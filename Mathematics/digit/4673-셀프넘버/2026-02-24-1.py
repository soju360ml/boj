# 에라토스테네스의 체 활용

import sys

input = sys.stdin.readline

data1 = [True] * 10001

for i in range(1, len(data1)):
    ans = i
    while i:
        ans += i % 10
        i //= 10
    if ans <= 10000:
        data1[ans] = False

for i in range(1, len(data1)):
    if data1[i] is True:
        print(i)