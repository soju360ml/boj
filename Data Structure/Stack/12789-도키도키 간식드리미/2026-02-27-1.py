import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
stack1 = []
cnt = 1
for i in arr:
    stack1.append(i)
    while stack1:
        if stack1[-1] == cnt:
            stack1.pop()
            cnt += 1
        else:
            break

if stack1:
    print('Sad')
else:
    print('Nice')