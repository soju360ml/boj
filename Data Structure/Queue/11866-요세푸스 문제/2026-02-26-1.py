import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())

source = collections.deque(list(range(1, N + 1)))
seq = []

i = 0
while source:
    if i == K - 1:
        seq.append(source.popleft())
    else:
        source.append(source.popleft())
    i = (i + 1) % K

print(f'<{', '.join(list(map(str, seq)))}>')