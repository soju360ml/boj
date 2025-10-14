# 2747 다이나믹 프로그래밍 피보나치

import sys
input = sys.stdin.readline

N = int(input())

records = {
    0: 0,
    1: 1
}

def dp(n):
    if n in records:
        return records[n]
    else:
        result = dp(n - 1) + dp(n - 2)
        records[n] = result
        return result
    
print(dp(N))