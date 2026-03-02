import sys
input = sys.stdin.readline

N = int(input())
ans = '666'
cnt = 0

i = 0
while cnt < N:
    i += 1
    if ans in str(i):
        cnt += 1

print(i)