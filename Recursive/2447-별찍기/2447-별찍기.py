import math

def recur(size):
    if size == 1:
        return ['*']
    else:
        pattern = []
        base = recur(size // 3)
        for i in base:
            pattern.append(i * 3)
        for i in base:
            pattern.append(i + ' ' * (size // 3) + i)
        for i in base:
            pattern.append(i * 3)
        return pattern

N = int(input())
result = recur(N)
for i in result:
    print(i)