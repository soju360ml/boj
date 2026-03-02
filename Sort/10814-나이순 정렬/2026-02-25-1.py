import sys
input = sys.stdin.readline

N = int(input())

data = [None] * N
for i in range(N):
    data[i] = input().split()

data.sort(key= lambda x: int(x[0]))

for i in data:
    print(*i)