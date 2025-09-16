# 11723 집합
# 백준 9663 N-Queen 문제를 해결하기 위한 비트마스킹 문제
import sys
input = sys.stdin.readline
M = int(input())
s = 0

def add(n):
    global s
    s |= 1 << n - 1

def remove(n):
    global s
    s &= ~(1 << n - 1)

def check(n):
    global s
    print(1 if s & 1 << n - 1 else 0)

def toggle(n):
    global s
    s ^= 1 << n - 1

def all():
    global s
    s = (1 << 20) - 1

def empty():
    global s
    s = 0
    
functions = {
    "add": add,
    "remove": remove,
    "check": check,
    "toggle": toggle,
    "all": all,
    "empty": empty
}

for _ in range(M):
    x = input().split()
    if len(x) == 2:
        functions[x[0]](int(x[1]))
    else:
        functions[x[0]]()