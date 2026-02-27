import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

stack1 = []
for _ in range(N):
    S = input().split()
    s = S[0]
    if len(S) == 2:
        v = S[1]

    if s == 'push':
        stack1.append(int(v))
    elif s == 'top':
        if stack1:
            print(stack1[-1])
        else:
            print(-1)
    elif s == 'size':
        print(len(stack1))
    elif s == 'empty':
        if stack1:
            print(0)
        else:
            print(1)
    elif s == 'pop':
        if stack1:
            print(stack1.pop())
        else:
            print(-1)