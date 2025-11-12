"""
입력
Input represents several test cases, followed by a line containing 0 0 0. Each test case has three positive integers, less than 30,000, denoting the lengths of the sides of a triangle.

출력
For each test case, a line containing "right" if the triangle is a right triangle, and a line containing "wrong" if the triangle is not a right triangle.

예제 입력 1 
6 8 10
25 52 60
5 12 13
0 0 0
예제 출력 1 
right
wrong
right
"""

import sys
input = sys.stdin.readline

boolean = []
while True:
    length = list(map(int, input().split()))
    if length[0] == 0 and length[1] == 0 and length[2] == 0:
        break
    else:
        length.sort()
        if length[0] ** 2 + length[1] ** 2 == length[2] ** 2:
            boolean.append("right")
        else:
            boolean.append("wrong")

for i in boolean:
    print(i)