import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
stack1 = []
cur = 1
for i in arr:
    if i == cur:
        cur += 1
        continue
    elif stack1 and stack1.pop() == cur:
        cur += 1
        continue
    else:
        stack1.append(i)

if stack1:
    print('Sad')
else:
    print('Nice')