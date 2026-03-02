# 가능한 모든 '조합'을 생성(브루트 포스) 후 최적의 해를 추출한다

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
lst1= list(map(int, input().split()))
lst2 = list(combinations(lst1, 3))
sum1 = [sum(i) for i in lst2]
sum1.sort(reverse=True)
for i in sum1:
    if i <= M:
        print(i)
        break