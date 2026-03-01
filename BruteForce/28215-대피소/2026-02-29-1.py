import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dist = {}
dist_max = {}

for _ in range(N):
    x, y = map(int, input().split())
    dist[(x, y)] = {}
    dist_max[(x, y)] = None

for k1 in dist:
    for k2 in dist:
        if k2 in dist[k1]: continue
        else:
            dist[k1][k2] = abs(k1[0] - k2[0]) + abs(k1[1] - k2[1])
            dist[k2][k1] = dist[k1][k2]


for k in dist:
    dist_max[k] = max(map(lambda x: dist[k][x], dist[k]))

for k1 in dist:
    for k2 in dist:
        print(f'dist[{k1}][{k2}]: {dist[k1][k2]}')
print(dist_max)