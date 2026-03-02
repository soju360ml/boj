import sys
import math

input = sys.stdin.readline

R, G = map(int, input().split())

a, b = R, G

while b:
    a, b = b, a % b

for i in range(1, int(math.sqrt(a)) + 1):
    if a % i == 0:
        print(i, R // i, G // i)
        if i != a // i:
            print(a // i, R // (a // i), G // (a // i))