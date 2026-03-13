import sys;read = sys.stdin.readline
import bisect

S = read().strip()
q = int(read())
alp = [[] for _ in range(26)]
for i in range(len(S)):
    alp[ord(S[i]) - 97].append(i)
    
for i in range(q):
    c, left, right = read().split()
    left, right = int(left), int(right)
    print(bisect.bisect_right(alp[ord(c) - 97], right) - bisect.bisect_left(alp[ord(c) - 97], left))