import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst = lst[:] + lst[:]
dic = { x : 0 for x in range(1, d + 1)}
s = set()

for i in range(k):
    dic[lst[i]] += 1
    s.add(lst[i])

dic[c] += 1
s.add(c)

ans = len(s)

for i in range(n - 1):
    left = i
    lnum = lst[left]
    dic[lnum] -= 1
    if dic[lnum] == 0:
        s.remove(lnum)

    right = i + k
    rnum = lst[right]
    dic[rnum] += 1
    s.add(rnum)
    ans = max(ans, len(s))
print(ans)