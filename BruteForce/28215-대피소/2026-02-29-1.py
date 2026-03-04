import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())

dist = {}

for _ in range(N):
    x, y = map(int, input().split())
    dist[(x, y)] = {}

combs = combinations(dist.keys(), K)

for k1 in dist:
    for k2 in dist:
        if k2 in dist[k1]: continue
        else:
            dist[k1][k2] = abs(k1[0] - k2[0]) + abs(k1[1] - k2[1])
            dist[k2][k1] = dist[k1][k2]

def dist_max():
    lst = []
    for comb in combs:
        tmp = []
        for pos in dist.keys():
            tmp.append(min(map(lambda x: dist[x][pos], comb)))
        lst.append(max(tmp))
    return min(lst)

print(dist_max())