"""
입력
첫 줄에 참가자의 수 $N$이 주어집니다. $(1 \le N \le 10^9)$ 

둘째 줄에 티셔츠 사이즈별 신청자의 수 $S, M, L, XL, XXL, XXXL$이 공백으로 구분되어 주어집니다. $(0 \le S, M, L, XL, XXL, XXXL \le N;$ $S + M + L + XL + XXL + XXXL = N)$ 

셋째 줄에 정수 티셔츠와 펜의 묶음 수를 의미하는 정수 $T$와 $P$가 공백으로 구분되어 주어집니다. $(2 \le T, P \le 10^9)$ 

출력
첫 줄에 티셔츠를 $T$장씩 최소 몇 묶음 주문해야 하는지 출력하세요.

다음 줄에 펜을 $P$자루씩 최대 몇 묶음 주문할 수 있는지와, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하세요.
"""

import sys
input = sys.stdin.readline

N = int(input())
sizeList = list(map(int, input().split()))
T, P = map(int, input().split())
Tpack = 0
Ppack = N // P
oneCount = N % P

for i in sizeList:
    if i > 0:
        if i > T:
            if i % T:
                Tpack += i // T + 1
            else:
                Tpack += i // T
        else:
            Tpack += 1

print(Tpack)
print(Ppack, oneCount)