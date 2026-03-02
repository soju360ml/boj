import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

def recur(n):
    if n == 0:
        return 1
    return n * recur(n - 1)

print(recur(N))