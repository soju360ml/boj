# 조합론

import sys
import math
from itertools import combinations
input = sys.stdin.readline

N = int(input())

print(math.perm(N, 2))